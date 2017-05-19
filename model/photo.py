#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

from google.appengine.ext import ndb


class Photo(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    title = ndb.StringProperty(required=True)
    image = ndb.BlobProperty()
    tags = ndb.StringProperty(repeated=True)
