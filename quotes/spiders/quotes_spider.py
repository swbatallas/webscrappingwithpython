import scrapy
from scrapy import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(20)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        divs = response.css("div.quote")
        for div in divs:
            yield {
                "quote" : div.css("span.text::text").get(),
                "author" : div.css("small.author::text").get(),
                "tags" : div.css("a.tag::text").getall()
                }