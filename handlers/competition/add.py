#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


from datetime import datetime
import logging
import webapp2

import handlers.general_tools as gentools
from model.member import Member
from model.competition import Competition
from model.participation_record import ParticipationRecord


class AddCompetitionHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr or not usr.is_admin():
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # Create competition
            competition = Competition(
                date=datetime.today(),
                date_inscription_closed=datetime.today(),
                name="Comp",
                type="Jornada",
                where="Ourense",
                map_position="",
                comments=""
            )

            competition_key = competition.put()

            # Create participation record
            participation_record = ParticipationRecord(
                competition=competition_key,
            )

            participation_record_key = participation_record.put()
            competition.participation_record = participation_record_key
            competition.put()
            self.redirect("/competition/modify?id=" + competition.key.urlsafe())
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))


app = webapp2.WSGIApplication([
    ("/competition/add", AddCompetitionHandler),
], debug=True)
