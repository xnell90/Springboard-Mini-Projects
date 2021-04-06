import scrapy

class XPathSpider(scrapy.Spider):
    name = "xpath-scraper"
    start_urls = [
        'https://www.w3.org/TR/xpath/all/',
    ]

    def parse(self, response):
        tags = {}
        for item in ['a', 'li', 'p']:
            tags[item] = response.css(item + '::text').getall()
        yield tags
