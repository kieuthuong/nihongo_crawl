import scrapy

class JobsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    