#!/usr/bin/env python
# (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member


class KernelHandler(webapp2.RequestHandler):
    def get(self):
        # Get user
        usr = Member.current()

        if (not usr
         or not usr.is_admin):
            return Member.show_error_unrecognized_usr(self)

        # Render
        try:
            jinja = jinja2.get_jinja2(app=self.app)
            template_values = { "usr": usr, "info": AppInfo }
            self.response.write(jinja.render_template("kernel.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))
        return


app = webapp2.WSGIApplication([
    ("/kernel", KernelHandler),
], debug=True)
