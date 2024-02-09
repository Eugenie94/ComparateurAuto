import scrapy
import json
from comparateurAuto.items import AutoItem


class SpoticarSpider(scrapy.Spider):
    name = "spoticar"
    allowed_domains = ["www.spoticar.fr"]
    start_urls = ["https://www.spoticar.fr/voitures-occasion/citroen-c3-bluehdi-100-ss-bvm5-feel-seine-maritime-le-grand-quevilly-1202944203"] #teste avec 1 voiture pour s'assurer que tous ok 


    def start_requests(self):
        # on récupère les liens dans le fichier json créé à partir de selenium
        json_file = 'C:/Users/mrmat/Documents/IPSSI-COURS/M2/web_scraping/tp_groupe/ComparateurAuto/comparateurAuto/spoticar_url.json'
        with open(json_file, 'r') as f:
            url_list = json.load(f)

        # parcourir les URL et envoyer une requête pour chacune d'entre elles
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        type_motorisation = ['essence', 'diesel', 'hybride', 'electrique']
        type_brand = ['audi', 'bmw', 'citroen', 'fiat', 'ford', 'mercedes', 'opel', 'peugeot', 'renault', 'toyota', 'volkswagen']
        volkswagen = ['golf', 'polo', 'passat', 'tiguan', 'touran', 'caddy', 'up', 'arteon', 't-cross', 't-roc', 'touareg', 'sharan', 'amarok', 'caravelle', 'multivan', 'california', 'transporter', 'crafter', 'id.3', 'id.4', 'id.buzz', 'id.space', 'id.vizzion', 'id.crozz', 'id.roomzz', 'id.buggy', 'id.buzz cargo', 'id.chrozz', 'id.life', 'id.streetmate', 'id.space vizzion', 'id.vizzion', 'id.buzz', 'id.buggy', 'id.crozz', 'id.life', 'id.roomzz', 'id.space vizzion', 'id.streetmate', 'id.vizzion']
        audi = ['a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'q2', 'q3', 'q5', 'q7', 'q8', 'tt', 'r8', 'etron', 'etron sportback', 'etron gt', 'etron s', 'etron gt', 'etron s', 'etron gt']
        bmw = ['serie 1', 'serie 2', 'serie 3', 'serie 4', 'serie 5', 'serie 6', 'serie 7', 'serie 8', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'z4', 'i3', 'i4', 'i8', 'm2', 'm3', 'm4', 'm5', 'm8', 'x3 m', 'x4 m', 'x5 m', 'x6 m', 'x7 m', 'z4 m']
        toyota = ['aygo', 'yaris', 'auris', 'corolla', 'avensis', 'prius', 'camry', 'gt86', 'c-hr', 'rav4', 'highlander', 'land cruiser', 'hilux', 'proace', 'proace verso', 'proace city', 'proace city verso', 'mirai', 'supra', 'urban cruiser', 'verso', 'iq', 'urban cruiser', 'verso', 'iq']
        peugeot = ['108', '208', '308', '508', '2008', '3008', '5008', 'traveller', 'partner', 'expert', 'boxer', 'ion', 'e-208', 'e-2008', 'e-208', 'e-2008']
        renault = ['twingo', 'clio', 'megane', 'scenic', 'kadjar', 'captur', 'koleos', 'zoe', 'twizy', 'fluence', 'espace', 'talisman', 'kangoo', 'trafic', 'master', 'zoe', 'twizy', 'fluence', 'espace', 'talisman', 'kangoo', 'trafic', 'master']
        citroen = ['c1', 'c3', 'c4', 'c5', 'c6', 'c8', 'berlingo', 'cactus', 'spacetourer', 'jumpy', 'jumper', 'ami', 'c-zero', 'e-c4', 'e-c4', 'e-c4']
        opel = ['adam', 'corsa', 'astra', 'insignia', 'mokka', 'crossland', 'grandland', 'combo', 'vivaro', 'movano', 'ampera', 'ampera-e', 'ampera', 'ampera-e']
        ford = ['ka', 'fiesta', 'focus', 'mondeo', 'kuga', 'ecosport', 'edge', 'puma', 'mustang', 'tourneo', 'transit', 's-max', 'galaxy', 'ranger', 'tourneo', 'transit', 's-max', 'galaxy', 'ranger']
        fiat = ['500', '500x', '500l', 'panda', 'punto', 'tipo', 'doblo', 'talento', 'ducato', 'qubo', 'fiorino', '500e', '500e']
        mercedes = ['a-klasse', 'b-klasse', 'c-klasse', 'e-klasse', 's-klasse', 'glc', 'gle', 'glb', 'glk', 'gl', 'g', 'v-klasse', 'vito', 'sprinter', 'eqa', 'eqb', 'eqc', 'eqe', 'eqs', 'eqv', 'eqa', 'eqb', 'eqc', 'eqe', 'eqs', 'eqv']
        type_gearbox = ['manuelle', 'automatique', 'semi-automatique']

        item = AutoItem()

        name_annonce =  response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.psa-fiche-vo-infovo.new_financing_gateway > div.psa-fiche-vo-infovo-padding.psa-fiche-vo-infovo-header > div.psa-fiche-vo-infovo-title > h1 > span.title.product-line::text").get().strip()
        name_annonce_split = name_annonce.split()
        year = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_matriculation_year > span::text").get().strip()
        price_section = response.css('#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.psa-fiche-vo-infovo.new_financing_gateway > div.psa-fiche-vo-infovo-padding.psa-fiche-vo-infovo-header > div.psa-fiche-vo-infovo-price-buy.psa-fiche-vo-infovo-price-buy-border-bottom > div > div > span::text').get().strip()
        price = int(price_section.replace('€', '').replace(' ', ''))
        mileage_section = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_mileage > span::text").get().strip()
        mileage = int(mileage_section.replace('km', '').replace(' ', ''))
        
        item['price'] = int(price)
        item['brand'] = name_annonce_split[0]
        item['model'] = name_annonce_split[1]
        item["year"] = int(year)
        item["mileage"] = int(mileage)
        item["engine_type"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_fuel > span::text").get().strip()
        item["gearbox"] = response.css("#full-vo > div.sidebar.psa-fiche-vo-header-info.col-lg-4.col-md-4.col-sm-12.col-xs-12.sidebar-fiche-vo-reskin.new_financing_gateway > div > div.content-button-main > div.summary-entries > div:nth-child(1) > div > div.summary-entrie.characteristic-item.field_vo_gear_box > span::text").get().strip()
        item["url"] = response.url


        yield item        