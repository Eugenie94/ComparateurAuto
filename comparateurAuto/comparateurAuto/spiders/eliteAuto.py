import scrapy

class EliteautoSpider(scrapy.Spider):
    name = "eliteAuto"
    allowed_domains = ["www.elite-auto.fr"]
    start_urls = ["https://www.elite-auto.fr/occasion"]

    def parse(self, response):

        # Extraction des données de la page actuelle

        ### Récupérer toutes les marques
        brand = response.css("p.grow > ais-highlight:nth-child(1) > span.ais-Highlight::text").extract()
        # for b in brand:
            # print(b)

        ### Récupérer tous les models
        modele = response.css("p.grow > ais-highlight:nth-child(2) > span.ais-Highlight::text").extract()
        # for m in modele:
            # print(m)

        ### Récupérer toutes les années
        year = response.css("div.tw-moto-details > span:nth-child(1)::text").extract()
        # for y in year:
            # print(y)

        ### Récupérer tous les kilométrages
        mileage = response.css("div.tw-moto-details > span:nth-child(2)::text").extract()
        # for m in mileage:
            # print(m)
        
        ### Récupérer tous les types d'essence
        engine_type = response.css("div.tw-moto-details > span:nth-child(3)::text").extract()
        # Permet de retirer tous les espaces pour afficher ma liste correctement
        engine_type_with_whitespace = [" ".join(etype.split()) for etype in engine_type]
        # for e in engine_type_with_whitespace:
            # print(e)

        ### Récupérer tous les gearbox
        gearbox = response.css("div.tw-moto-details > span:nth-child(4)::text").extract()
        # for g in gearbox:
            # print(g)

        ### Récupérer tous les prix
        price = response.css("div.tw-offer-card-price:nth-child(2)::text").extract()
        # for p in price:
            # print(p)

        ### Récupérer toutes les urls
        url = response.css("span.app-algolia-card > div.w-full > a.tw-globalTag::attr(href)").extract()
        for u in url:
            print(u)

        yield {
                "marque": brand,
                "model": modele,
                "année": year,
                "kilométrage": mileage,
                "type": engine_type,
                "boite vitesse" : gearbox,
                "prix": price,
                "url": url
            }
        
        # # Suivre le lien vers la page suivante
        # next_page = response.css("a.tw-pagination-item[aria-label='Page suivante']::attr(href)").extract_first()
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)