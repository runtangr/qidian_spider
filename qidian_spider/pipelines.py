# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from qidian_spider.model.book import Book


class QidianSpiderMongodbPipeline(object):

    def process_item(self, item, spider):

        book = Book(**(item._values))
        book.save()

