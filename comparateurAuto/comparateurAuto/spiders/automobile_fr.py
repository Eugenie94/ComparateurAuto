import scrapy


class AutomobileFrSpider(scrapy.Spider):
    name = "automobile_fr"
    allowed_domains = ["www.automobile.fr"]
    start_urls = ["https://www.automobile.fr/"]

    def parse(self, response):
        brand = response.css("div::text").extract()
        pass
