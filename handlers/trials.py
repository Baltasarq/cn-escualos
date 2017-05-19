#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.trial import Trial


class TrialsHandler(webapp2.RequestHandler):
    def get(self):
        trials = Trial.query().order(Trial.date)

        template_values = {
            "info": AppInfo,
            "trials": trials,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("trials.html", **template_values))

app = webapp2.WSGIApplication([
    ('/trials', TrialsHandler)
], debug=True)
