import scrapy
from qidian_spider.items import QidianSpiderItem
from scrapy.http import Request


class QidianSpider(scrapy.Spider):
    name = "qidian"
    download_delay = 6
    allowed_domains = ["qidian.com"]
    rank_urls = "https://www.qidian.com/rank/{0}/?page={1}"
    rank_tuple = ("yuepiao", "hotsales", "newvipclick")

    def start_requests(self):
        for i in self.rank_tuple:
            url = self.rank_urls.format(i, 1)
            yield Request(url, self.parse)

    def parse(self, response):

        books = response.xpath('//div[@class="book-img-text"]/ul/li')
        for book in books:

            item = QidianSpiderItem()

            book_name = book.xpath('div[@class="book-mid-info"]/h4/a/text()').extract()
            book_auth = book.xpath('div[@class="book-mid-info"]/p/a[1]/text()').extract()
            book_type = book.xpath('div[@class="book-mid-info"]/p/a[2]/text()').extract()
            book_status = book.xpath('div[@class="book-mid-info"]/p[@class="author"]/span/text()').extract()
            book_brief = book.xpath('div[@class="book-mid-info"]/p[@class="intro"]/text()').extract()
            num_type = book.xpath('div[@class="book-right-info"]/div/p/text()').extract()
            num = book.xpath('div[@class="book-right-info"]/div/p/span/text()').extract()

            item["book_name"] = book_name
            item["book_auth"] = book_auth
            item["book_type"] = book_type
            item["book_status"] = book_status
            item["book_brief"] = book_brief
            item["num_type"] = num_type
            item["num"] = num

            yield item

            max_num = response.xpath('//div[@id="page-container"]/@data-pagemax')[0].extract()
            for page_num in range(2, int(max_num)+1):

                url = response.url.split('=')[0] + '=' + str(page_num)
                yield Request(url, self.parse)
