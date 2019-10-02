#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from datetime import datetime
from webapp2_extras import jinja2

import handlers.general_tools as gentools
from model.member import Member
from model.swim_styles import SwimStyles
from model.appinfo import AppInfo
from model.competition import Competition
from model.participation_record import ParticipationRecord


class OpenCompetitionsForMemberHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr:
            Member.show_error_unrecognized_usr(self)
            return

        # Gather competitions
        today = datetime.today()
        competitions = Competition.query(Competition.date_inscription_closed >= today).fetch()

        # Fetch participation_records
        participation_record_keys = []
        for competition in competitions:
            prs = ParticipationRecord.query(ParticipationRecord.competition == competition.key).fetch(keys_only=True)

            if len(prs) > 0:
                participation_record_keys.append(prs[0])

        try:
            # User info
            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles,
                "competitions": competitions,
                "participation_record_keys": participation_record_keys,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("open_competitions_for_member.html", **data))
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/member/open_competitions", OpenCompetitionsForMemberHandler),
], debug=True)