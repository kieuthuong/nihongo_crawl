# -*- coding: utf-8 -*-
import scrapy 
from nguonsukien.items import NguonsukienItem
class QuotesSpider(scrapy.Spider):
	name = "sukien"
	start_urls=[ #dia chi bat dau cho spider
		'http://vneconomy.vn/chung-khoan.htm',
		'http://hastc.org.vn/chung-khoan',
	]
	def parse(self, response):
		news_vneconomy = response.xpath('//div[@class="infonews"]/a/@href').extract()
		news_hastc = response.xpath('//h2[@class="entry-title"]/a/@href').extract()
		list = [news_vneconomy,news_hastc]
		hastc_link = "http://hastc.org.vn"
		for links in list:
        	for x in links:
        		if x.:
        			pass
				link = "http://vneconomy.vn"+x
				yield scrapy.Request(link, callback=self.saveFile)
	def saveFile(self, response):
		if :
			pass
		tieuDe = response.xpath('//h1[@class="title"]/text()').extract()
		noiDung = response.xpath('//div[@class="contentdetail"]/p/text()').extract()
		ngay = response.xpath('//p[@class="time"]/text()').extract()
		print(tieuDe)
		print(noiDung)
		print(ngay)