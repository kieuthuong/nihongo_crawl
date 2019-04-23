from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from jobs.items import JobsItem

class MySpider(BaseSpider):
    name = "tst"
    allowed_domains = ["vietnamworks.com"]
    start_urls = ["https://www.vietnamworks.com/viec-lam-tai-ha-noi-v24-vn","https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//div[@class='bold-red' or @class=' ']")
        items = []
        for titles in titles:
            item = JobsItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items