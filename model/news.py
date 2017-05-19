#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

from google.appengine.ext import ndb


class News(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    title = ndb.StringProperty(required=True)
    url = ndb.StringProperty()
    body = ndb.StringProperty()
