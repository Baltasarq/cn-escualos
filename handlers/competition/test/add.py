#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
import time

import handlers.general_tools as gentools
from model.member import Member
from model.swim_styles import SwimStyles
from model.competition import Competition
from model.competition import Test


class AddCompetitionTestHandler(webapp2.RequestHandler):
    def post(self):
        # Check if the user is logged in
        usr = Member.current()

        if not usr or not usr.is_admin():
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # Assign data to this competition
            competition = Competition.retrieve_competition(self)

            distance = gentools.int_from_str(self.request.get("edDistance", "0"))
            style_abbrev = self.request.get("edStyle", "")
            is_relayed = (self.request.get("edRelayed", "off") == "on")
            str_gender = (self.request.get("edGender", "0"))
            str_day = self.request.get("edDay", "1")
            str_session = self.request.get("edSession", "0")

            try:
                gender = int(str_gender)
            except:
                return self.redirect("/error?msg=Adding new test to competition, gender cannot be: " + str_gender)

            if distance < 25:
                return self.redirect("/error?msg=Adding new test to competition, distance cannot be: " + str(distance) + "m.")

            if not style_abbrev:
                return self.redirect("/error?msg=Adding new test to competition: style not found.")

            competition.add_new_test(
                gentools.int_from_str(str_day),
                gentools.int_from_str(str_session),
                distance,
                SwimStyles.id_from_abbrev(style_abbrev),
                is_relayed,
                gender
            )

            competition.put()
            time.sleep(1)
        except Exception as e:
            logging.error(gentools.error_from_exception(e))
            return self.redirect("/error?msg=Storing competition: " + str(e))

        # Send a response
        self.redirect("/competition/modify?id=" + competition.key.urlsafe())
        return


app = webapp2.WSGIApplication([
    ("/competition/test/add", AddCompetitionTestHandler),
], debug=True)
