import scrapy


class AutomobileFrSpider(scrapy.Spider):
    name = "automobile_fr"
    allowed_domains = ["www.automobile.fr"]
    start_urls = ["https://www.automobile.fr/cat%C3%A9gorie/voiture/vhc:car,pgn:10,pgs:10,dmg:false"]

    def parse(self, response):
        brand = response.css("article:nth-child(2) > div > div.g-row.js-ad-entry > a > div.g-col-s-12.g-col-m-8 > div.vehicle-text.g-row > h3").extract()
        print(brand)


