import scrapy


class CnSpider(scrapy.Spider):
    name = 'cn'
    allowed_domains = ['www.uniqlo.cn']
    start_urls = ['http://www.uniqlo.cn/']

    def parse(self, response):
        pass
