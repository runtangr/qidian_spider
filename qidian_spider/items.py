# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    auth = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    brief = scrapy.Field()
    num_type = scrapy.Field()
    num = scrapy.Field()
    rank = scrapy.Field()
    rank_type = scrapy.Field()
