import scrapy
from comparateurAuto.items import AutoItem


class HolyroadSpider(scrapy.Spider):
    name = "holyroad"
    allowed_domains = ["hollyroad.fr"]
    start_urls = ["https://hollyroad.fr"]

    def start_requests(self):
        base_url = "https://hollyroad.fr/resultats-de-recherche?gad_source=1&gclid=CjwKCAiAt5euBhB9EiwAdkXWO2oarJMiGJmnjl6I53a4TDAgfkYXu2Ah1rD5huAwatqx9JeGlC-BNxoC_KgQAvD_BwE&currentpage={}"
        # page_number = 46000
        for page_number in range(35, 46000):
            url = base_url.format(page_number)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = AutoItem()
        cars = response.css("div.search-result")
        for car in cars:
            car_name = car.css("div.wrapper-title > div.title > p::text").get()
            item["brand"] = car_name.split()[0]
            item["model"] = car_name.split()[1]
            item["year"] = int(car.css("div.wrapper-year  div.info-description  p::text").get().strip())
            car_mileage = car.css("div.wrapper-km  div.info-description  p::text").get().strip()
            item["mileage"] = int(car_mileage.replace('Km', '').replace(' ', ''))
            item["engine_type"] = car.css("div.wrapper-engine  div.info-description  p::text").get().strip()
            item["gearbox"] = car.css("div.wrapper-gear  div.info-description  p::text").get().strip()
            item["price"] = int(car.css("div.wrapper-price  div.price  p::text").get().strip().replace('€', '').replace(' ', ''))
            item["url"] = car.css("div.wrapper-button > a::attr(href)").get()
            yield item
        
