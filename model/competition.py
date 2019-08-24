#!/usr/bin/env python
# (c) CNEscualos Baltasar 2016/19 MIT License <baltasarq@gmail.com>


from model.record_entry import SwimStyles

from google.appengine.ext import ndb


class Test(ndb.Model):
    distance = ndb.IntegerProperty(required=True)
    style_id = ndb.IntegerProperty(required=True)
    is_relay = ndb.BooleanProperty(default=False)

    def get_style_name(self):
        return SwimStyles.name_from_id(self.style_id)

    def __str__(self):
        return (str(self.distance) + "m " + self.get_style_name()
                + (" relevos" if self.is_relay else ""))


class Competition(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    date = ndb.DateProperty(indexed=True, required=True)
    date_inscription_closed = ndb.DateProperty(indexed=True, required=True)
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty()
    where = ndb.StringProperty()
    map_position = ndb.StringProperty()
    comments = ndb.StringProperty()
    tests = ndb.StructuredProperty(Test, repeated=True)

    @staticmethod
    def retrieve_competition(req):
        id = None
        try:
            id = req.request.GET["id"]
        except ValueError:
            req.redirect("/error?msg=Missing competition id.")

        try:
            competition = ndb.Key(urlsafe=id).get()
        except:
            req.redirect("/error?msg=No competition for id: " + str(id))

        return competition
