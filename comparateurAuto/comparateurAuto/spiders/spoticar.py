import scrapy
import json
from comparateurAuto.items import AutoItem


class SpoticarSpider(scrapy.Spider):
    name = "spoticar"
    allowed_domains = ["www.spoticar.fr"]
    start_urls = ["https://www.spoticar.fr/voitures-occasion/citroen-c3-bluehdi-100-ss-bvm5-feel-seine-maritime-le-grand-quevilly-1202944203"] #teste avec 1 voiture pour s'assurer que tous ok 


    def start_requests(self):
        # on récupère les liens dans le fichier json créé à partir de selenium
        json_file = '../../spoticar_url.json'
        with open(json_file, 'r') as f:
            url_list = json.load(f)

        # parcourir les URL et envoyer une requête pour chacune d'entre elles
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        item = AutoItem()

        item["model"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.psa-fiche-vo-infovo.new_financing_gateway > div.psa-fiche-vo-infovo-padding.psa-fiche-vo-infovo-header > div.psa-fiche-vo-infovo-title > h1 > span.title.product-line::text").get().strip()
        item["year"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_matriculation_year > span::text").get().strip()
        item["mileage"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_mileage > span::text").get().strip()
        item["engine_type"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_fuel > span::text").get().strip()
        item["price"] = response.css('#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.psa-fiche-vo-infovo.new_financing_gateway > div.psa-fiche-vo-infovo-padding.psa-fiche-vo-infovo-header > div.psa-fiche-vo-infovo-price-buy.psa-fiche-vo-infovo-price-buy-border-bottom > div > div > span::text').get().strip() 
        item["gearbox"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_gear_box > span::text").get().strip()
        item["brand"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.psa-fiche-vo-infovo.new_financing_gateway > div.psa-fiche-vo-infovo-padding.psa-fiche-vo-infovo-header > div.psa-fiche-vo-infovo-title > h1 > span.title.product-finish::text").get().strip()
        item["url"] = response.url


        yield item        