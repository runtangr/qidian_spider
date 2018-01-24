import scrapy
from qidian_spider.items import QidianSpiderItem
from scrapy.http import Request


class QidianSpider(scrapy.Spider):
    name = "qidian"
    download_delay = 6
    allowed_domains = ["qidian.com"]
    rank_urls = "https://www.qidian.com/rank/{0}/?page={1}"
    rank_tuple = ("yuepiao", "newvipclick")

    def start_requests(self):
        for i in self.rank_tuple:
            url = self.rank_urls.format(i, 1)
            yield Request(url, self.parse)

    def parse(self, response):

        books = response.xpath('//div[@class="book-img-text"]/ul/li')
        for book in books:

            item = QidianSpiderItem()

            book_name = book.xpath('div[@class="book-mid-info"]/h4/a/text()')[0].extract()
            book_auth = book.xpath('div[@class="book-mid-info"]/p/a[1]/text()')[0].extract()
            book_type = book.xpath('div[@class="book-mid-info"]/p/a[2]/text()')[0].extract()
            book_status = book.xpath('div[@class="book-mid-info"]/p[@class="author"]/span/text()')[0].extract()
            book_brief = book.xpath('div[@class="book-mid-info"]/p[@class="intro"]/text()')[0].extract()
            num_type = book.xpath('div[@class="book-right-info"]/div/p/text()')[0].extract()
            num = book.xpath('div[@class="book-right-info"]/div/p/span/text()')[0].extract()
            rank = book.xpath('@data-rid')[0].extract()

            item["name"] = book_name
            item["auth"] = book_auth
            item["type"] = book_type
            item["status"] = book_status
            item["brief"] = book_brief
            item["num_type"] = num_type
            item["num"] = int(num)
            item["rank"] = int(rank)

            # get rank type
            item["rank_type"] = response.url.split('/')[-2]

            yield item

            max_num = response.xpath('//div[@id="page-container"]/@data-pagemax')[0].extract()
            for page_num in range(2, int(max_num)+1):

                url = response.url.split('=')[0] + '=' + str(page_num)
                yield Request(url, self.parse)
