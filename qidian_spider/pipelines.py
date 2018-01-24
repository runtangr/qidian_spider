# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from model.book import Book


class QidianSpiderPipeline(object):

    def process_item(self, item, spider):

        a = item._values
        book = Book(**(item._values))
        book.save()
        # print(item)
