import scrapy
from comparateurAuto.items import AutoItem            
import json

class EliteautoSpider(scrapy.Spider):
    name = "eliteAuto"
    allowed_domains = ["www.elite-auto.fr"]
    start_urls = ["https://www.elite-auto.fr/occasion"]

    def start_requests(self):
            # Définir les URLs de départ pour chaque page
            base_url = "https://www.elite-auto.fr/recherche?prod_ELITE_OFFERS%5Bpage%5D={}&prod_ELITE_OFFERS%5BrefinementList%5D%5Bcategory%5D%5B0%5D=1&prod_ELITE_OFFERS%5BsortBy%5D=prod_ELITE_OFFERS_occasion&prod_ELITE_OFFERS%5BhitsPerPage%5D=100"
            total_pages = 1000

            for page_number in range(1, total_pages + 1):
                url = base_url.format(page_number)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # Extraction des données de la page actuelle

        ### Récupérer tous les articlees
        articles = response.css("app-algolia-card")
        item = AutoItem()

        # Itérer sur chaque article
        for article in articles:
            # Récupérer les données spécifiques de chaque article
            brand = article.css("p.grow > ais-highlight:nth-child(1) > span.ais-Highlight::text").get()
            model = article.css("p.grow > ais-highlight:nth-child(2) > span.ais-Highlight::text").get()
            year = article.css("div.tw-moto-details > span:nth-child(1)::text").extract()
            mileage = article.css("div.tw-moto-details > span:nth-child(2)::text").extract()
            engine_type = article.css("div.tw-moto-details > span:nth-child(3)::text").extract()
            engine_type_split = [" ".join(etype.split()) for etype in engine_type]
            gearbox = article.css("div.tw-moto-details > span:nth-child(4)::text").extract()
            price = article.css("div.tw-offer-card-price:nth-child(2)::text").extract()
            url = article.css("a.tw-globalTag::attr(href)").extract()

            # Création de l'instance de autoItem
            item["brand"] = brand
            item["model"] = model
            item["year"] = year
            item["mileage"] = mileage
            item["engine_type"] = engine_type_split
            item["gearbox"] = gearbox
            item["price"] = price
            item["url"] = url
            print(model)
            # yield item
