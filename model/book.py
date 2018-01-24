# -*- coding: utf-8 -*-
from mongoengine import *


class Book(Document):
    __tablename__ = 'book'

    name = StringField()
    auth = StringField()
    type = StringField()
    status = StringField()
    brief = StringField()
    num_type = StringField()
    num = IntField()
    rank = IntField()
    rank_type = StringField()
