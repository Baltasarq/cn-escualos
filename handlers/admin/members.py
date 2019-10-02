#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Patreons of the club


import logging
from datetime import datetime
import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member


class KernelMembersHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Get current user, must be admin
            usr = Member.current()

            if (not usr
             or not usr.is_admin()):
                return Member.show_error_unrecognized_usr(self)

            # Get user to modify
            chosen_usr_key = self.request.GET.get("id")

            if not chosen_usr_key:
                chosen_usr = usr
            else:
                chosen_usr = ndb.Key(urlsafe=chosen_usr_key).get()

            # Get all members
            members = Member.query(Member.active == True).order(Member.surname)

            # Render
            template_values = {
                "info": AppInfo,
                "members": members,
                "usr": usr,
                "chosen_usr": chosen_usr,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("kernel_members.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))

    def post(self):
        try:
            # Get current user, must be admin
            usr = Member.current()

            if (not usr
             or not usr.is_admin()):
                return Member.show_error_unrecognized_usr(self)

            # Determine add or modify
            member_dni = self.request.get("edDNI", "").strip().upper()
            member = Member.query(Member.dni == member_dni).get()

            if not member:
                member = Member(
                    birth=datetime(year=1970, month=1, day=1),
                    dni="0A",
                    lic=-1,
                    soc=0,
                    active=True,
                    surname="Doe",
                    name="John")

            try:
                member_key = Member.assign_data(member, self.request)
            except Exception as e:
                logging.error("Storing usr", str(e))
                return self.redirect("/error?msg=Storing usr: " + str(e))

            return self.redirect("/admin/members?id=" + member_key.urlsafe())
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ("/admin/members", KernelMembersHandler),
], debug=True)
