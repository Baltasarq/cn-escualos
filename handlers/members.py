#!/usr/bin/env python
# MIT License
# (c) baltasar 2016


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member


class MembersHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Get current user, but anyway this section is public
            usr = Member.current()

            # Get all members
            members = Member.query(Member.active == True).order(Member.surname)

            # Render
            template_values = {
                "info": AppInfo,
                "members": members,
                "usr": usr
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("members.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/members', MembersHandler)
], debug=True)
