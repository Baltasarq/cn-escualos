#!/usr/bin/env python
# (c) CNEscualos baltasar 2016/19 MIT License <baltasarq@gmail.com>

from google.appengine.ext import ndb

from model.photo import Photo
from model.document import Document


class News(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    title = ndb.StringProperty(required=True)
    body = ndb.StringProperty()
    url = ndb.StringProperty()                              # Optional
    photo = ndb.KeyProperty(kind=Photo, default=None)       # Optional
    doc = ndb.KeyProperty(kind=Document, default=None)      # Optional
