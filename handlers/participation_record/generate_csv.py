#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Generates participation record as CSV


import webapp2
from webapp2_extras import jinja2

from model.participation_record import ParticipationRecord
from model.elapsed_time_distance import ElapsedTimeDistance


class GenerateMembersCSVHandler(webapp2.RequestHandler):
    def get(self):
        # Retrieve participation record
        participation_record = ParticipationRecord.retrieve_participation_record(self)
        competition = participation_record.competition.get()

        # Tests
        tests = {}
        for test in competition.tests:
            tests[test.uid] = test

        # Members
        members = {}
        for participant in participation_record.participants:
            member = participant.member.get()
            members[member.key] = member

        template_values = {
            "participation_record": participation_record,
            "ElapsedTimeDistance": ElapsedTimeDistance,
            "competition": competition,
            "tests": tests,
            "members": members,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.headers['Content-Type'] = "text/csv"
        self.response.headers['Content-Disposition'] = "attachment; filename=cnescualos-registro_participation.csv"
        self.response.write(jinja.render_template("participation_record_data.csv", **template_values))
        return


app = webapp2.WSGIApplication([
    ("/participation_record/generate_csv", GenerateMembersCSVHandler),
], debug=True)
