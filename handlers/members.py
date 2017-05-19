#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member


class MembersHandler(webapp2.RequestHandler):
    def get(self):
        members = Member.query(Member.active == True).order(Member.surname)

        template_values = {
            "info": AppInfo,
            "members": members,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("members.html", **template_values))


app = webapp2.WSGIApplication([
    ('/members', MembersHandler)
], debug=True)
