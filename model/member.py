#!/usr/bin/env python
# CNEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


import time
import logging
from datetime import date
from datetime import datetime

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import images

import handlers.general_tools as gentools
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
    email = ndb.StringProperty(default=None, indexed=True)
    records = ndb.StructuredProperty(RecordEntry, repeated=True)
    comments = ndb.StringProperty()
    photo = ndb.BlobProperty()

    def is_admin(self):
        return users.is_current_user_admin()

    @staticmethod
    def set_admin():
        admin = Member.query(Member.dni == "ADMIN").get()

        if not admin:
            admin = Member(
                dni="ADMIN",
                active=False,
                birth=datetime(year=2015, month=6, day=17),
                comments="admin",
                soc=2015061700,
                lic=0,
                name="admin",
                surname="root",
                photo=None)

        admin.email = users.get_current_user().email()
        admin.put()
        time.sleep(1)

        admin.gae_usr = users.get_current_user()
        return admin

    @staticmethod
    def current():
        toret = None
        gae_usr = users.get_current_user()

        if gae_usr:
            gae_usr_email = gae_usr.email().strip().lower()
            toret = Member.query(Member.email == gae_usr_email).get()

            if toret:
                toret.gae_usr = gae_usr

        return toret

    @staticmethod
    def show_error_unrecognized_usr(handler):
        gae_usr = users.get_current_user()
        usr_name = "anonymous" if not gae_usr else gae_usr.email()

        return handler.redirect("/error?msg=Usuario no reconocido: '" + usr_name + "'")

    @staticmethod
    def assign_data(member, request):
        # Retrieve data
        member_dni = request.get("edDNI", "").strip().upper()
        member_birth = request.get("edBirth", "2001-01-01")
        member_surname = request.get("edSurname", "").strip()
        member_name = request.get("edName", "").strip()
        member_lic = gentools.int_from_str(request.get("edLic", "-1"))
        member_soc = gentools.int_from_str(request.get("edSoc", str(member.soc)))
        member_comments = request.get("edComments", "").strip()
        member_photo = request.get("edPhoto", None)
        member_active = request.get("edActive", "no")
        member_email = request.get("edEmail", str(member.email)).strip().lower()

        if (not member_dni
         or not member_email
         or not member_name
         or not member_surname
         or not member_soc):
            raise Exception("Missing or wrong data creating/modifying member.")

        # Store
        try:
            if member_photo: member.photo = images.resize(member_photo, 64, 64)
        except images.Error as e:
            logging.error("Member photo was not added: " + type(e).__name__ + ' ' + str(e))

        if member_dni: member.dni = member_dni
        if member_birth: member.birth = datetime.strptime(member_birth, "%Y-%m-%d")
        if member_lic >= 0: member.lic = member_lic
        if member_soc >= 0: member.soc = member_soc
        if member_name: member.name = member_name
        if member_surname: member.surname = member_surname
        if member_comments: member.comments = member_comments

        member.active = member_active.strip() == "yes"
        member.email = member_email
        key = member.put()
        time.sleep(1)

        return key
