#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging
import webapp2

import handlers.general_tools as gentools
from model.member import Member
from model.competition import Competition


class DeleteCompetitionHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr or not usr.is_admin:
            Member.show_error_unrecognized_usr(self)
            return

        try:
            competition = Competition.retrieve_competition(self)
            # participation_record = ParticipationRecord(competition_key == competition.key)

            # participation_record.key.delete()
            competition.key.delete()
            time.sleep(1)
            return self.redirect("/competition/management")
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/competition/delete", DeleteCompetitionHandler),
], debug=True)
