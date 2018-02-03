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
   'scrapy_crawlera.CrawleraMiddleware': 300
}


ITEM_PIPELINES = {
   'qidian_spider.pipelines.QidianSpiderMongodbPipeline': 300,
}

REDIS_URL = 'redis://10.10.1.58:6379'

# scrapy_redis set
DUPEFILTER_CLASS = "qidian_spider.scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "qidian_spider.scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = False
SCHEDULER_QUEUE_CLASS = "qidian_spider.scrapy_redis.queue.SpiderPriorityQueue"

# crawlera set
CRAWLERA_ENABLED = True
CRAWLERA_USER = 'eee92c3deb124898828b37a5bf93dbd2'
CRAWLERA_PASS = ''


CRAWLERA_PRESERVE_DELAY = True
