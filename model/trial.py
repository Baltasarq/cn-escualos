#!/usr/bin/env python
# (c) CNEscualos Baltasar 2016/19 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb


class Trial(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    date = ndb.DateProperty(indexed=True)
    name = ndb.StringProperty(required=True)
    comments = ndb.StringProperty()
    poster = ndb.BlobProperty()
