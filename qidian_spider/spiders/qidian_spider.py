import scrapy
from qidian_spider.items import QidianSpiderItem
from scrapy.http import Request


class QidianSpider(scrapy.Spider):
    name = "qidian"
    download_delay = 6
    allowed_domains = ["qidian.com"]
    start_urls = [
        "https://www.qidian.com/all"
    ]

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



    # def parse(self, response):
    #
    #     books = response.xpath('//div[@class="book-img-text"]/ul/li')
    #     for book in books:
    #
    #         qidian_item = QidianSpiderItem()
    #
    #         qidian_item["book_name"] = book.xpath('div[@class="book-info "]/h1/em/text()')[0].extract()
    #         qidian_item["auth"] = book.xpath('div[@class="book-mid-info"]/p/a[1]/text()')[0].extract()
    #         qidian_item["type"] = book.xpath('div[@class="book-mid-info"]/p/a[2]/text()')[0].extract()
    #         qidian_item["status"] = book.xpath('div[@class="book-mid-info"]/p[@class="author"]/span/text()')[0].extract()
    #         qidian_item["brief"] = book.xpath('div[@class="book-mid-info"]/p[@class="intro"]/text()')[0].extract()
    #         qidian_item["grade"] = book.xpath('div[@class="book-right-info"]/div/p/text()')[0].extract()
    #         qidian_item["comment_num"] = book.xpath('div[@class="book-right-info"]/div/p/span/text()')[0].extract()
    #         qidian_item['book_covor_image_url']  = book.xpath('@data-rid')[0].extract()
    #
    #         # get rank type
    #         item["rank_type"] = response.url.split('/')[-2]
    #
    #         yield item
    #
    #         max_num = response.xpath('//div[@id="page-container"]/@data-pagemax')[0].extract()
    #         for page_num in range(2, int(max_num)+1):
    #
    #             url = response.url.split('=')[0] + '=' + str(page_num)
    #             yield Request(url, self.parse)
