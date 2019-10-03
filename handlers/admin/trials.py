#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Trails organized by the club


import time
import logging
import webapp2
from google.appengine.api import images
from webapp2_extras import jinja2
from datetime import datetime

from model.appinfo import AppInfo
from model.trial import Trial
from model.member import Member


class TrialsHandler(webapp2.RequestHandler):
    def get(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not usr.is_admin()):
            return Member.show_error_unrecognized_usr(self)

        # Render trials
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "trials": Trial.query().order(-Trial.date).fetch()
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("kernel_trials.html", **template_values));
        except Exception as e:
            logging.error("rendering trials", str(e))
            self.response.write("ERROR: " + str(e))

    def post(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not (usr.is_admin())):
            return Member.show_error_unrecognized_usr(self)

        # Get the data
        name = self.request.get("edName", "").strip()
        comments = self.request.get("edComments", "").strip()
        str_date = self.request.get("edDate", str(datetime.today().date()))

        if not name:
            return self.redirect("/error?msg=Prueba sin nombre")

        try:
            date = datetime.strptime(str_date, "%Y-%m-%d")
        except:
            date = datetime.today().date()

        poster = None
        try:
            poster_data = self.request.get("edPoster", None)

            if poster_data:
                img_poster = images.Image(poster_data)
                width = img_poster.width
                height = img_poster.height
                new_width = (400 * width) / height
                poster = images.resize(poster_data, new_width, 400)
        except images.Error as e:
            logging.error("Getting image", str(e))

        trial = Trial(name=name, date=date, comments=comments)
        if poster:
            trial.poster = poster

        trial.put()
        time.sleep(1)
        return self.redirect("/admin/trials")


app = webapp2.WSGIApplication([
    ("/admin/trials", TrialsHandler),
], debug=True)
