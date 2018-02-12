# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    auth = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    brief = scrapy.Field()

    book_covor_image_url = scrapy.Field()
    original_url = scrapy.Field()
    book_id = scrapy.Field()
    score = scrapy.Field()
    comment_num = scrapy.Field()
