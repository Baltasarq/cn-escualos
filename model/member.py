#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

from datetime import date
from google.appengine.ext import ndb


class Member(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    birth = ndb.DateProperty(required=True, default=date(1970, 1, 1))
    dni = ndb.StringProperty(required=True, indexed=True)
    lic = ndb.IntegerProperty(required=True)
    soc = ndb.IntegerProperty(required=True, indexed=True)
    active = ndb.BooleanProperty(required=True,indexed=True,default=True)
    surname = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True)
    comments = ndb.StringProperty()
    photo = ndb.BlobProperty()
