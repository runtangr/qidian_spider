# -*- coding: utf-8 -*-

from mongoengine import connect

import redis

DBSession = connect("qidain_spider")

Redis = redis.StrictRedis(host='localhost', port=6379, db=0)
