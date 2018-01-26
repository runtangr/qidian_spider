# -*- coding: utf-8 -*-


BOT_NAME = 'qidian_spider'

SPIDER_MODULES = ['qidian_spider.spiders']
NEWSPIDER_MODULE = 'qidian_spider.spiders'

DOWNLOAD_DELAY = 1
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
   # 'qidian_spider.middlewares.QidianSpiderDownloaderMiddleware': 543,
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
   'qidian_spider.contrib.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   'qidian_spider.pipelines.QidianSpiderPipeline': 300,
}

REDIS_URL = 'redis://10.10.1.58:6379'


DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
