import scrapy

class AramisautoSpider(scrapy.Spider):
    name = "aramisAuto"
    allowed_domains = ["https://www.aramisauto.com/achat/"]
    start_urls = ["https://www.aramisauto.com/achat/"]

    def parse(self, response):
        # Récupérer tous les éléments h2 de la page
        h2_elements = response.css("h2::text").extract()

        # Imprimer les textes des éléments h2
        for h2_text in h2_elements:
            print(h2_text)

        # Vous pouvez également stocker ou traiter les données d'une autre manière ici
