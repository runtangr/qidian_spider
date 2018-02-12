import scrapy
from qidian_spider.items import QidianSpiderItem
from scrapy.http import Request
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.remote_connection import LOGGER
import logging

LOGGER.setLevel(logging.WARNING)


class QidianSpider(scrapy.Spider):
    name = "qidian"
    allowed_domains = ["qidian.com"]
    start_urls = [
        "https://www.qidian.com/all"
    ]

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        self.driver.set_window_size(1080, 800)
        super(QidianSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        if response.status == 400:
            time.sleep(2)
            # failing page and again request
            yield Request(url=response.url, callback=self.parse, dont_filter=True)
            return
        try:
            next_table = response.xpath('//a[contains(@class, "lbf-pagination-next")]')[0].extract()
        except IndexError:
            # failing page and again request
            yield Request(url=response.url, callback=self.parse, dont_filter=True)
            return

        try:
            next_link_url = response.xpath('//a[contains(@class, "lbf-pagination-next")]/@href')[0].extract()
        except IndexError:
            # end
            return

        if next_link_url:
            yield Request(url="https://" + next_link_url, callback=self.parse)

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
        book_id = response.url.split('/')[-1]
        qidian_item['book_id'] = book_id

        # add grade and comment number by selenium
        self.driver.get(response.url)
        wait = WebDriverWait(self.driver, timeout=300)
        score = ''
        comment_num = ''
        wait_result = wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="j_bookScore"]'),
            '.'))
        if wait_result is True:
            score = self.driver.find_element_by_xpath('//*[@id="j_bookScore"]').text
            comment_num = self.driver.find_element_by_xpath('//*[@id="j_userCount"]').text

        qidian_item['score'] = score
        qidian_item['comment_num'] = comment_num

        yield qidian_item
