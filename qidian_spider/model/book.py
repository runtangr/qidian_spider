# -*- coding: utf-8 -*-
from mongoengine import *
import datetime


class Book(Document):
    __tablename__ = 'book'

    book_name = StringField()
    auth = StringField()
    type = ListField()
    status = StringField()
    brief = StringField()
    book_covor_image_url = StringField()
    original_url = StringField()
    book_id = StringField()
    update_time = DateTimeField(default=datetime.datetime.utcnow())

    score = StringField()
    comment_num = StringField()

