#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Patreons of the club


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member


class KernelMembersHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Get current user, must be admin
            usr = Member.current()

            if (not usr
             or not usr.is_admin):
                return Member.show_error_unrecognized_usr(self)

            # Get all members
            members = Member.query(Member.active == True).order(Member.surname)

            # Render
            template_values = {
                "info": AppInfo,
                "members": members,
                "usr": usr
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
                    or not usr.is_admin):
                return Member.show_error_unrecognized_usr(self)

            # Save
            new_member = Member()
            try:
                Member.assign_data(new_member, self.request)
            except Exception as e:
                logging.error("Storing usr", str(e))
                return self.redirect("/error?msg=Storing usr: " + str(e))

            return self.redirect("/admin/members")
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ("/admin/members", KernelMembersHandler),
], debug=True)
