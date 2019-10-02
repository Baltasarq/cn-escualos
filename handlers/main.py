#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.appinfo import AppInfo
from model.news import News
from model.member import Member
from model.patreon import Patreon


class MainHandler(webapp2.RequestHandler):
    def get(self):
        login_url = ""
        usr = Member.current()
        news = News.query().order(-News.added).fetch(limit=3)

        if not usr:
            login_url = users.create_login_url("/ensure_login")

        template_values = {
            "info": AppInfo,
            "news": news,
            "usr": usr,
            "login_url": login_url,
            "patrons": Patreon.query()
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
