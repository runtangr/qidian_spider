# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from qidian_spider.model.book import Book
from scrapy import log


class QidianSpiderMongodbPipeline(object):

    def process_item(self, item, spider):

        book = Book(**(dict(item)))
        try:
            result = book.save()
        except:
            log.msg("Item save mongodb fail!",
                    level=log.ERROR, spider=spider)
            return item
        log.msg("Item %s wrote to mongodb database qidain_spider/book" %
                (str(result.id)),
                level=log.DEBUG, spider=spider)
        return item


