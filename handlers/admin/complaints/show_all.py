#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016/19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member
from model.complaint import Complaint


class ShowComplaintsHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Get current user, but anyway this section is public
            usr = Member.current()

            # Get all members
            complaints = Complaint.query().order(-Complaint.added)

            # Render
            template_values = {
                "info": AppInfo,
                "complaints": complaints,
                "usr": usr
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("show_all_complaints.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/admin/complaints/show_all', ShowComplaintsHandler)
], debug=True)
