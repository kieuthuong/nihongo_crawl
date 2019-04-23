# -*- coding: utf-8 -*-
import scrapy 
from nhaccuatui.items import NhaccuatuiItem
class QuotesSpider(scrapy.Spider):
	name = "lyric"#khi run chi dinh name di crawl
	start_urls=[ #dia chi bat dau cho spider
		'https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html'
	]

	def parse(self, response):
		finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-1].extract()
		totalPage = int(finalPage.split(".")[-2])
		for page in range(totalPage):
			link = finalPage.replace(str(totalPage), str(page + 1))
			yield scrapy.Request(link, callback=self.crawlLyric)
	def crawlLyric(self, response):
		for linkLyric in response.xpath('//a[@class="name_song"]/@href').extract():
			yield scrapy.Request(linkLyric, callback=self.saveFile)
	def saveFile(self, response):
		lyricRaw = response.xpath('//p[@class="pd_lyric trans"]/text()').extract()
		lyric = "\n".join(lyricRaw[1:])
		item = NhaccuatuiItem()
		item['name'] = lyricRaw[0].encode("utf-8")
		item['lyric'] = lyric.encode("utf-8")
		item['link'] = response.url.encode("utf-8")
		yield item