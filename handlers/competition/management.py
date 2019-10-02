#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

import handlers.general_tools as gentools
from model.member import Member
from model.competition import Competition
from model.participation_record import ParticipationRecord
from model.appinfo import AppInfo


class ManageCompetitionsHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr or not usr.is_admin():
            Member.show_error_unrecognized_usr(self)
            return

        try:
            competitions = Competition.query().order(-Competition.date)

            data = {
                "info": AppInfo,
                "usr": usr,
                "competitions": competitions,
                "ParticipationRecord": ParticipationRecord
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("competitions.html", **data))
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/competition/management", ManageCompetitionsHandler),
], debug=True)
