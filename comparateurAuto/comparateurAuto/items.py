import scrapy

class ComparateurautoItem(scrapy.Item):
    model = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    engine_type = scrapy.Field()
    price = scrapy.Field()
    gearbox = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()