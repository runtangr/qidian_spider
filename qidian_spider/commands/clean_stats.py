# -*-coding:utf-8-*-

import redis

# default values
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
STATS_KEY = 'scrapy:stats'


def clear_stats():
    server = redis.Redis(REDIS_HOST, REDIS_PORT)
    server.delete(STATS_KEY)


if __name__ == "__main__":
    clear_stats()