import scrapy

class CssSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://www.w3.org/TR/selectors',
    ]

    def parse(self, response):
        a_texts = response.css("a::text").getall()
        tob_counter = {} # table of contents counter
        for a_text in a_texts:
            if '§' in a_text:
                if a_text in tob_counter:
                    tob_counter[a_text[1:]] += 1
                else:
                    tob_counter[a_text[1:]] = 1

        yield tob_counter
