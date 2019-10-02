#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging

import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member
from model.swim_styles import SwimStyles
from model.participation_record import ParticipationRecord
from model.elapsed_time_distance import ElapsedTimeDistance

import handlers.general_tools as gentools


class ModifyParticipationRecordHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr or not usr.is_admin():
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # Competition info
            participation_record = ParticipationRecord.retrieve_participation_record(self)
            competition = participation_record.competition.get()

            # Competition stats
            total_participants = len(participation_record.participants)
            num_lunchers = len(
                [participant
                 for participant in participation_record.participants if participant.stays_for_lunch])

            # Tests
            tests = competition.tests
            tests.sort(key=lambda test: (test.style_id * 100000) + test.distance)
            participants_per_test = {}

            for test in tests:
                participants_per_test[test.uid] = \
                    [x for x in participation_record.participants_per_test if x.test_uid == test.uid]

            # Render answer
            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles,
                "ElapsedTimeDistance": ElapsedTimeDistance,
                "tests": tests,
                "competition": competition,
                "members": Member.query().order(Member.surname).order(Member.name).fetch(),
                "participation_record": participation_record,
                "participants_per_test": participants_per_test,
                "num_lunchers": num_lunchers,
                "total_participants": total_participants
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("edit_participation_record.html", **data))
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/participation_record/modify", ModifyParticipationRecordHandler),
], debug=True)
