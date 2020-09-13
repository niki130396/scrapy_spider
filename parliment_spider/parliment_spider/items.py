# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParlimentSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    first_name = scrapy.Field()
    middle_name = scrapy.Field()
    last_name = scrapy.Field()
    birth_date = scrapy.Field()
    birth_place = scrapy.Field()
    profession = scrapy.Field()
    languages = scrapy.Field()
    political_party = scrapy.Field()
    email_address = scrapy.Field()
