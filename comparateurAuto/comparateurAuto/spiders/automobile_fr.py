import scrapy


class AutomobileFrSpider(scrapy.Spider):
    name = "automobile_fr"
    allowed_domains = ["www.automobile.fr"]
    start_urls = ["https://www.automobile.fr/"]

    def parse(self, response):
        
        pass
