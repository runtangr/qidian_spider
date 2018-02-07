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
   'qidian_spider.contrib.downloadmiddleware.rotate_proxy.ProxyMiddleware': 400,
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

# set polipo
HTTP_PROXY = 'http://127.0.0.1:8787'


HTTPERROR_ALLOWED_CODES = [400]

# log
LOG_LEVEL = 'DEBUG'
LOG_FILE = "logs/scrapy.log"
LOG_FORMATTER = 'qidian_spider.scrapy.logformatter.LogFormatter'

# graphite
STATS_CLASS = 'qidian_spider.graphite.graphite.RedisGraphiteStatsCollector'
GRAPHITE_HOST = '127.0.0.1'
GRAPHITE_PORT = 2003

