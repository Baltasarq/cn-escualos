#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.trial import Trial
from model.member import Member


class TrialsHandler(webapp2.RequestHandler):
    def get(self):
        # User info, though not required
        usr = Member.current()

        # Get relevant trials
        trials = Trial.query().order(-Trial.date)

        # Render
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "trials": trials,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("trials.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/trials', TrialsHandler)
], debug=True)
