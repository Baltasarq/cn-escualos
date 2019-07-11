#!/usr/bin/env python
# CNEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


import datetime
from datetime import date
from google.appengine.ext import ndb
from google.appengine.api import users


from model.record_entry import RecordEntry


class Member(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    birth = ndb.DateProperty(required=True, default=date(1970, 1, 1))
    dni = ndb.StringProperty(required=True, indexed=True)
    lic = ndb.IntegerProperty(required=True)
    soc = ndb.IntegerProperty(required=True, indexed=True)
    active = ndb.BooleanProperty(required=True, indexed=True, default=False)
    surname = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty(required=True, indexed=True)       # Google user id: usr.user_id()
    identified = ndb.BooleanProperty(required=True, default=False)  # True if already identified
    is_admin = ndb.BooleanProperty(required=True, default=False)    # Is it admin?
    records = ndb.StructuredProperty(RecordEntry, repeated=True)
    comments = ndb.StringProperty()
    photo = ndb.BlobProperty()

    @staticmethod
    def retrieve_usr_data():
        toret = None
        gae_usr = users.get_current_user()

        if gae_usr:
            list_usrs_found = Member.query(Member.user_id == gae_usr.user_id()).fetch()

            if (list_usrs_found
            and len(list_usrs_found) > 0):
                toret = list_usrs_found[0]

        return toret

    @staticmethod
    def current():
        """Returns the current user, or None.
            :return: The Member object for the current user, or None.
        """

        toret = Member.retrieve_usr_data()
        gae_usr = users.get_current_user()

        if users.is_current_user_admin():
            if not toret:
                toret = Member()
                toret.birth = datetime.datetime.now()
                toret.dni = "0A"
                toret.lic = 0
                toret.soc = 0
                toret.surname = "swimmer"
                toret.name = gae_usr.nickname()
                toret.user_id = gae_usr.user_id()
                toret.identified = True
                toret.is_admin = True
                toret.active = True
                toret.comments = "admin"
                toret.photo = None
                toret.put()
        else:
            if (not toret
             or not toret.identified
             or not toret.is_admin):
                toret = None

        if toret:
            toret.gae_usr = gae_usr

        return toret

    @staticmethod
    def show_error_unrecognized_usr(handler):
        gae_usr = users.get_current_user()
        usr_name = "anonymous" if not gae_usr else gae_usr.email()

        handler.redirect("/error?msg=Unrecognized user: " + usr_name)
        return
