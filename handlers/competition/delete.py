#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging
import webapp2

import handlers.general_tools as gentools
from model.member import Member
from model.competition import Competition
from model.participation_record import ParticipationRecord


class DeleteCompetitionHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr or not usr.is_admin():
            Member.show_error_unrecognized_usr(self)
            return

        try:
            competition = Competition.retrieve_competition(self)

            # Remove the competition itself
            competition_key = competition.key
            competition_key.delete()
            time.sleep(1)

            # Remove participation record
            try:
                participation_record = ParticipationRecord.query(ParticipationRecord.competition == competition.key).get()

                if participation_record:
                    participation_record.key.delete()
            except:
                logging.error("ERROR: Participation record was not found for competition: " + str(competition_key))

            return self.redirect("/competition/management")
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/competition/delete", DeleteCompetitionHandler),
], debug=True)
