# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class BeikeItem(Item):
    house_name = Field()
    sale_status = Field()
    house_type = Field()
    house_address = Field()
    house_price = Field()

    # pass
