#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

from google.appengine.ext import ndb


class Document(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    title = ndb.StringProperty(required=True)
    file = ndb.BlobProperty()
    tags = ndb.StringProperty(repeated=True)
