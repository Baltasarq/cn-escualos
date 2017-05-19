#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.news import News


class NewsHandler(webapp2.RequestHandler):
    def get(self):
        news = News.query().order(-News.added)

        template_values = {
            "info": AppInfo,
            "news": news,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("news.html", **template_values))

app = webapp2.WSGIApplication([
    ('/news', NewsHandler)
], debug=True)
