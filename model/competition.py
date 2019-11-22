#!/usr/bin/env python
# (c) CNEscualos Baltasar 2016/19 MIT License <baltasarq@gmail.com>


import time
from google.appengine.ext import ndb

from model.swim_styles import SwimStyles


class Test(ndb.Model):
    SESSIONS = ["matutina", "de tarde"]
    TEST_GENDERS = ["masculino", "femenino", "mixto"]

    uid = ndb.IntegerProperty(required=True, default=-1)
    distance = ndb.IntegerProperty(required=True)
    style_id = ndb.IntegerProperty(required=True)
    is_relay = ndb.BooleanProperty(default=False)
    day = ndb.IntegerProperty(default=1)
    session = ndb.IntegerProperty(default=0)
    gender = ndb.IntegerProperty(default=0)

    def is_male(self):
        return self.gender == 0

    def is_female(self):
        return self.gender == 1

    def is_mixed(self):
        return self.gender == 2

    def get_gender_as_string(self):
        return Test.TEST_GENDERS[self.gender]

    def get_style_name(self):
        return SwimStyles.name_from_id(self.style_id)

    def str_from_session(self):
        return Test.SESSIONS[self.session]

    def str_min_desc(self):
        return ((" Relevos " if self.is_relay else " ")
                + (str(self.distance) + "m " + self.get_style_name())
                + " " + self.get_gender_as_string())

    def __str__(self):
        return ("Jornada " + str(self.day)
                + " (" + self.str_from_session() + ")"
                + self.str_min_desc())


class Competition(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    date = ndb.DateProperty(indexed=True, required=True)
    date_inscription_closed = ndb.DateProperty(indexed=True, required=True)
    name = ndb.StringProperty(indexed=True, required=True)
    type = ndb.StringProperty()
    where = ndb.StringProperty()
    map_position = ndb.StringProperty()
    comments = ndb.StringProperty()
    tests = ndb.StructuredProperty(Test, repeated=True)

    def get_sorted_tests(self):
        toret = self.tests
        toret.sort(key=lambda test: (test.day * 1000000) + (test.session * 100000)
                                        + test.distance + (test.style_id * 10) + test.gender)
        return toret

    def add_new_test(self, day, session, distance, style_id, is_relay, gender):
        uid = int(time.time())

        test = Test(
            uid=uid,
            day=day,
            session=session,
            distance=distance,
            style_id=style_id,
            is_relay=is_relay,
            gender=gender)

        self.tests.append(test)
        return uid

    def delete_test_with_uid(self, uid):
        test = self.look_for_test_with_uid(uid)

        if test:
            self.tests.remove(test)

        return

    def look_for_test_with_uid(self, uid):
        toret = None

        if uid is not None:
            for test in self.tests:
                if test.uid == uid:
                    toret = test
                    break

        return toret

    @staticmethod
    def retrieve_competition(req):
        id = None
        try:
            id = req.request.GET["id"]
        except ValueError:
            return req.redirect("/error?msg=Missing competition id.")

        try:
            competition = ndb.Key(urlsafe=id).get()
        except:
            return req.redirect("/error?msg=No competition for id: " + str(id))

        return competition
