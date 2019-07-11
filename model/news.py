#!/usr/bin/env python
# (c) CNEscualos baltasar 2016/19 MIT License <baltasarq@gmail.com>

from google.appengine.ext import ndb


class News(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    title = ndb.StringProperty(required=True)
    url = ndb.StringProperty()
    body = ndb.StringProperty()
    photo_id = ndb.IntegerProperty()
