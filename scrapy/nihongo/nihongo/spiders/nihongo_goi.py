import scrapy
import re
#coding=UTF8
from nihongo.items import NihongoItem
class QuotesSpider(scrapy.Spider):
	"""docstring for QuotesSprider"""
	name = "goi"
	start_urls = [
		'https://www.vnjpclub.com/minna-no-nihongo/?fbclid=IwAR1HuApAW-wcJbtmhxrQKEhriFU5u3-RgkJpvIMcMYfcVkm1PMghtDD7RfU'
	]
	def parse(self,response):
		finalPage = response.xpath('//form[@id="adminForm"]/table/tbody/tr[51]/td/a/@href')[-1].extract()
		#finalPage1 = finalPage.replace('-','.')
		#totalPage = int(finalPage1.split(".")[-2])
		totalPage = int(re.split('\.|-',finalPage)[-2])
		for page in range(totalPage):
			link = finalPage.replace(str(totalPage), str(page + 1))
			link1="https://www.vnjpclub.com"+link
			yield scrapy.Request(link1, callback=self.crawlGoi)
	def crawlGoi(self,response):
		for linkGoi in response.xpath('//a[@id="tuvung"]/@href').extract():
			linkGoi1="https://www.vnjpclub.com"+linkGoi
			yield scrapy.Request(linkGoi1, callback=self.saveFile)
	def saveFile(self,response):
		goi_japanese = response.xpath('//div[@id="rt-mainbody"]/div/article/div/table/tbody/tr/td[1]/text()').extract()
		goi_vietnamese = response.xpath('//div[@id="rt-mainbody"]/div/article/div/table/tbody/tr/td[5]/text()').extract()
		item = NihongoItem()	
		dictionary = dict(zip(goi_japanese, goi_vietnamese))
		print(dictionary)
		