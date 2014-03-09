from scrapy.item import Item, Field

class FivethClassItem(Item):
    image_urls = Field()
    images = Field()
