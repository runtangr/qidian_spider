import scrapy
from qidian_spider.items import QidianSpiderItem
from scrapy.http import Request

from scrapy_redis.spiders import RedisSpider


class QidianSpider(RedisSpider):
    name = "qidian"
    download_delay = 6
    allowed_domains = ["qidian.com"]
    # start_urls = [
    #     "https://www.qidian.com/all"
    # ]
    redis_key = 'qidian_spider:start_urls'

    def parse(self, response):

        next_link = response.xpath('//a[@class="lbf-pagination-next "]/@href')[0].extract()

        if next_link:
            yield Request(url="https://" + next_link, callback=self.parse)

        for detail_link in response.xpath('//div[@class="book-mid-info"]/h4/a/@href').extract():
            if detail_link:

                yield Request(url="https://" + detail_link, callback=self.parse_detail)

    def parse_detail(self, response):
        qidian_item = QidianSpiderItem()

        qidian_item["book_name"] = response.xpath('//div[@class="book-info "]/h1/em/text()')[0].extract()
        qidian_item["auth"] = response.xpath('//div[@class="book-info "]/h1/span/a/text()')[0].extract()

        qidian_item["type"] = response.xpath('//div[@class="book-info "]/p[@class="tag"]/a/text()').extract()
        qidian_item["status"] = response.xpath('//div[@class="book-info "]/p/span/text()')[0].extract()
        qidian_item["brief"] = response.xpath('//div[@class="book-info "]/p[@class="intro"]/text()')[0].extract()
        qidian_item['book_covor_image_url'] = "https:" + response.xpath('//div[@class="book-img"]/a/img/@src')[0].extract()

        qidian_item['original_url'] = response.url

        yield qidian_item
