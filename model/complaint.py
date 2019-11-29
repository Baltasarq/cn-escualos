#!/usr/bin/env python
# (c) CNEscualos Baltasar 2016/19 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb

from model.member import Member


class Complaint(ndb.Model):
    added = ndb.DateTimeProperty(auto_now_add=True, indexed=True, required=True)
    author = ndb.KeyProperty(kind=Member, required=True, indexed=True)
    text = ndb.TextProperty(default="")
