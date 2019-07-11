#!/usr/bin/env python
# CnEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb


class Patreon(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    photo = ndb.BlobProperty()
    name = ndb.StringProperty(required=True, indexed=True)
    url = ndb.StringProperty()
