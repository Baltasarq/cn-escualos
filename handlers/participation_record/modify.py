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
            num_lunchers = 0
            num_companions = 0

            for participant in participation_record.participants:
                num_companions += participant.num_companions

                if participant.stays_for_lunch:
                    num_lunchers += 1 + participant.num_companions

            # Tests
            tests = competition.get_sorted_tests()
            participants_per_test = {}

            for test in tests:
                participants_per_test[test.uid] = \
                    [x for x in participation_record.participants_per_test if x.test_uid == test.uid]

            # Sorted participants
            participants = participation_record.participants
            participants.sort(key=lambda p: p.member.get().surname)

            # Render answer
            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles,
                "ElapsedTimeDistance": ElapsedTimeDistance,
                "tests": tests,
                "competition": competition,
                "members": Member.query().order(Member.surname).order(Member.name).fetch(),
                "participants": participants,
                "participation_record": participation_record,
                "participants_per_test": participants_per_test,
                "num_lunchers": num_lunchers,
                "total_participants": total_participants,
                "num_companions": num_companions,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("edit_participation_record.html", **data))
            logging.info("*** Template rendered")
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/participation_record/modify", ModifyParticipationRecordHandler),
], debug=True)
