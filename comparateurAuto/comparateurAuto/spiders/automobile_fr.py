import scrapy
from comparateurAuto.items import AutoItem
import re
import time
import time

class AutomobileFrSpider(scrapy.Spider):
    name = "automobile_fr"
    allowed_domains = ["www.automobile.fr"]
    def start_requests(self):
        base_url = "https://www.automobile.fr/catégorie/voiture/vhc:car,pgn:{},pgs:10,dmg:false"
        page_number = 1
        while True:
            yield scrapy.Request(url=base_url.format(page_number), callback=self.parse)
            page_number += 1
            time.sleep(1)  # Add a delay of 1 second

    def parse(self, response):
        item = AutoItem()
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

        vehicles = response.css("article.list-entry")

        for vehicle in vehicles:
            name_annonces = vehicle.css("h3.vehicle-title::text").extract()
            price = vehicle.css("div.vehicle-prices > p::text").extract()
            section_mileage = vehicle.css("div.vehicle-information > p::text").extract()
            year = vehicle.css("div.vehicle-information > p::text").extract()
            url = vehicle.css("a.vehicle-data::attr(href)").extract()
            section_engine_type = vehicle.css("div.vehicle-techspecs > p:first-child::text").extract()
            
            price_split = price[0]

            price_pattern = r'(\d[\d\s]+)€'

            price_matches = re.findall(price_pattern, price_split)
            if price_matches:
                price_int = int("".join(price_matches[0].split()))
                item['price'] = price_int
            item['url'] = url
            
            mileage_split = section_mileage[0].split()
            item['mileage'] = int(mileage_split[1] + mileage_split[2])
            item['year'] = int(mileage_split[0][-5:].replace(',', ''))
        
            for element in section_engine_type:
                element_to_lower = element.lower()
                element_split = element_to_lower.split()
                element_split_replace = [word.replace(',', '') for word in element_split]
                for word in element_split_replace:
                    if word in type_motorisation:
                        engine_type = word
                        item['engine_type'] = engine_type
                for word in element_split_replace:
                    if word in type_gearbox:
                        gearbox = word
                        item['gearbox'] = gearbox      

            for element in name_annonces:
                element_to_lower = element.lower()
                element_split = element_to_lower.split()
                for word in element_split:
                    if word in type_brand:
                        brand = word
                        item['brand'] = brand
        
            for element in name_annonces:
                element_to_lower = element.lower()
                element_split = element_to_lower.split()
                for word in element_split:
                    if word in volkswagen:
                        model = word
                        item['model'] = model  
                    elif word in audi:
                        model = word
                        item['model'] = model  
                    elif word in bmw:
                        model = word
                        item['model'] = model  
                    elif word in toyota:
                        model = word
                        item['model'] = model  
                    elif word in peugeot:
                        model = word
                        item['model'] = model  
                    elif word in renault:
                        model = word
                        item['model'] = model  
                    elif word in citroen:
                        model = word
                        item['model'] = model  
                    elif word in opel:
                        model = word
                        item['model'] = model  
                    elif word in ford:
                        model = word
                        item['model'] = model  
                    elif word in fiat:
                        model = word
                        item['model'] = model  
                    elif word in mercedes:
                        model = word
                        item['model'] = model  
            yield item
       
    