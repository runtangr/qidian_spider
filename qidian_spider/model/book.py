# -*- coding: utf-8 -*-
from mongoengine import *


class Book(Document):
    __tablename__ = 'book'

    book_name = StringField()
    auth = StringField()
    type = ListField()
    status = StringField()
    brief = StringField()
    book_covor_image_url = StringField()
    original_url = StringField()

