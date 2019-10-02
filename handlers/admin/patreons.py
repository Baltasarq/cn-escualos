#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Patreons of the club


import time
import logging
import webapp2
from google.appengine.api import images
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member
from model.patreon import Patreon


class PatreonsHandler(webapp2.RequestHandler):
    def get(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not usr.is_admin()):
            return Member.show_error_unrecognized_usr(self)

        # Render patreons
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "patreons": Patreon.query()
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("patreons.html", **template_values));
        except Exception as e:
            logging.error("rendering patreons", str(e))
            self.response.write("ERROR: " + str(e))

    def post(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not (usr.is_admin())):
            return Member.show_error_unrecognized_usr(self)

        # Get the data
        name = self.request.get("edName", "").strip()

        if not name:
            return self.redirect("/error?msg=Patrocinador sin nombre")

        url = self.request.get("edUrl", "")
        photo = None
        try:
            edImg = self.request.get("edPhoto", None)

            if edImg:
                photo = images.resize(edImg, 64, 64)
        except images.Error as e:
            logging.error("Getting image", str(e))

        patreon = Patreon(name=name, url=url)
        if photo:
            patreon.photo = photo

        patreon.put()
        time.sleep(1)
        return self.redirect("/admin/patreons")


app = webapp2.WSGIApplication([
    ("/admin/patreons", PatreonsHandler),
], debug=True)
