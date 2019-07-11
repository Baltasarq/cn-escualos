#!/usr/bin/env python
# MIT License
# (c) baltasar 2016


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.news import News
from model.member import Member


class NewsHandler(webapp2.RequestHandler):
    def get(self):
        # Current user, though not required
        usr = Member.current()

        # Get relevant news
        news = News.query().order(-News.added)

        # Render
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "news": news,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("news.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/news', NewsHandler)
], debug=True)
