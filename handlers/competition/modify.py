#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging
import webapp2
from datetime import datetime
from webapp2_extras import jinja2

import handlers.general_tools as gentools
from model.member import Member
from model.competition import Competition
from model.appinfo import AppInfo
from model.record_entry import SwimStyles


class ModifyCompetitionHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr or not usr.is_admin:
            Member.show_error_unrecognized_usr(self)
            return

        try:
            competition = Competition.retrieve_competition(self)

            # Render answer
            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles,
                "competition": competition
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("edit_competition.html", **data))
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))

    def post(self):
        # Check if the user is logged in
        usr = Member.current()

        if not usr or not usr.is_admin:
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # Assign data to this competition
            competition = Competition.retrieve_competition(self)

            date = self.request.get("edDate", "2001-01-01")
            expiration_date = self.request.get("edExpirationDate", "2001-01-01")
            name = self.request.get("edName", "Comp")
            comp_type = self.request.get("edType", "Jornada")
            where = self.request.get("edWhere", "Ourense")
            map_position = self.request.get("edMapPoint", "http://maps.google.com/")
            comments = self.request.get("edComments", "")

            competition.date = datetime.strptime(date, "%Y-%m-%d")
            competition.date_inscription_closed = datetime.strptime(expiration_date, "%Y-%m-%d")
            competition.name = name
            competition.type = comp_type
            competition.where = where
            competition.map_position = map_position
            competition.comments = comments

            competition.put()
            time.sleep(1)
            self.redirect("/competition/modify?id=" + competition.key.urlsafe())
        except Exception as e:
            logging.error("Storing competition", str(e))
            return self.redirect("/error?msg=Storing competition: " + str(e))


app = webapp2.WSGIApplication([
    ("/competition/modify", ModifyCompetitionHandler),
], debug=True)
