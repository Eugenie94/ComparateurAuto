import scrapy

class ComparateurautoItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    engine_type = scrapy.Field()
    gearbox = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()