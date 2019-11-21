#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging

import webapp2
from google.appengine.ext import ndb

from model.member import Member
from model.participation_record import ParticipationRecord


class DeleteMemberParticipationForParticipationRecordHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Determine origin
            org = self.request.GET.get("org")

            if not org:
                org = "admin"

            # Retrieve participant index
            str_participant_key = self.request.GET.get("member_id")

            if str_participant_key:
                try:
                    participant_key = ndb.Key(urlsafe=str_participant_key)
                except:
                    msg = "Deleting participant: converting participant key."
                    logging.error(msg)
                    return self.redirect("/error?msg=" + msg)
            else:
                return self.redirect("/error?msg=Not enough data deleting member participation.")

            # Check if the user is logged in
            usr = Member.current()

            if not usr or (not usr.is_admin() and usr.key != participant_key):
                Member.show_error_unrecognized_usr(self)
                return

            # Remove participation data
            participation_record = ParticipationRecord.retrieve_participation_record(self)
            participation_record.remove_member(participant_key)
            participation_record.put()

            return_address = "/member/participation_record?id="
            if org == "admin" and usr.is_admin():
                return_address = "/participation_record/modify?id="

            return self.redirect(return_address + participation_record.key.urlsafe())
        except Exception as e:
            logging.error("Deleting member participation in participation_record", str(e))
            return self.redirect("/error?msg=Deleting member participation in participation record: " + str(e))


app = webapp2.WSGIApplication([
    ("/participation_record/member_participation/delete", DeleteMemberParticipationForParticipationRecordHandler),
], debug=True)
