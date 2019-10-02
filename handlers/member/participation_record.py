#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.member import Member
from model.appinfo import AppInfo
from model.competition import SwimStyles
from model.participation_record import ParticipationRecord
from model.elapsed_time_distance import ElapsedTimeDistance


class MemberParticipationRecordHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Get current user
            usr = Member.current()

            if not usr:
                return self.redirect("/error?msg=User not recognized.")

            # Participation record data
            participation_record = ParticipationRecord.retrieve_participation_record(self)
            competition = participation_record.competition.get()
            tests = competition.tests
            tests.sort(key=lambda test: (test.style_id * 1000000) + test.distance)

            # Member's participation
            member_participation = None

            for participant in participation_record.participants:
                if participant.member == usr.key:
                    member_participation = participant
                    break

            # Member's tests
            member_participation_in_tests = {}

            for test in tests:
                member_participation_in_tests[test.uid] = \
                    [x for x in participation_record.participants_per_test
                                    if x.test_uid == test.uid and x.member == usr.key]

            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles,
                "ElapsedTimeDistance": ElapsedTimeDistance,
                "competition": competition,
                "tests": tests,
                "participation_record": participation_record,
                "member_participation": member_participation,
                "member_participation_in_tests": member_participation_in_tests
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("edit_member_participation_record.html", **data))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ("/member/participation_record", MemberParticipationRecordHandler),
], debug=True)
