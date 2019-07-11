#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
import time
from datetime import datetime
from google.appengine.api import images
from webapp2_extras import jinja2

import handlers.general_tools as gentools
from model.member import Member
from model.record_entry import SwimStyles
from model.appinfo import AppInfo


class ModifyMemberHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr:
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # User info
            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("user.html", **data))
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))

    def post(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr:
            return Member.show_error_unrecognized_usr(self)

        # Retrieve data
        try:
            member_dni = self.request.get("edDNI", "")
            member_birth = self.request.get("edBirth", "2000-01-01")
            member_surname = self.request.get("edSurname", "")
            member_name = self.request.get("edName", "")
            member_lic = int(self.request.get("edLic", "-1"))
            member_comments = self.request.get("edComments", "")
            member_photo = self.request.get("edPhoto", None)
            member_active = self.request.get("edActive", "no")
        except Exception as e:
            logging.error(gentools.error_from_exception(e))
            return self.redirect("/error?msg=Retrieving member info: " + gentools.error_from_exception(e))

        # Store
        try:
            if member_photo: usr.photo = images.resize(member_photo, 64, 64)
        except images.Error as e:
            logging.error("Member photo was not added: " + type(e).__name__ + ' ' + str(e))

        try:
            if member_dni: usr.dni = member_dni
            if member_birth: usr.birth = datetime.strptime(member_birth, "%Y-%m-%d")
            if member_lic: usr.lic = member_lic
            if member_name: usr.name = member_name
            if member_surname: usr.surname = member_surname
            if member_comments: usr.comments = member_comments

            usr.active = member_active.strip() == "yes"

            usr.put()
            time.sleep(1)

            # Send a response
            self.redirect("/members/modify")
            return
        except Exception as e:
            logging.error(gentools.error_from_exception(e))
            self.redirect("/error?msg=Storing member: " + gentools.error_from_exception(e))

        return


app = webapp2.WSGIApplication([
    ("/members/modify", ModifyMemberHandler),
], debug=True)
