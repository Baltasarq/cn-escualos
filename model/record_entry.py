#!/usr/bin/env python
# CNEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb


from model.elapsed_time_distance import ElapsedTimeDistance


class RecordEntry(ElapsedTimeDistance):
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    where = ndb.StringProperty()
