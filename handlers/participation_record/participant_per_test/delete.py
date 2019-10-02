#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging

import webapp2

from model.member import Member
from model.participation_record import ParticipationRecord


class DeleteMemberTestForParticipationRecordHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Retrieve org
            org = self.request.GET.get("org")

            if not org:
                org = "admin"

            # Retrieve participant index
            str_participant_per_test_uid = self.request.GET.get("member_test_id")
            participant_per_test_uid = -1

            if str_participant_per_test_uid:
                try:
                    participant_per_test_uid = int(str_participant_per_test_uid)
                except ValueError:
                    msg = "Deleting participant per test: converting participant index, assuming zero."
                    logging.error(msg)
                    self.redirect("/error?msg=" + msg)
            else:
                return self.redirect("/error?msg=Not enough data deleting member-test participation.")

            # Retrieve the participant per test data
            participation_record = ParticipationRecord.retrieve_participation_record(self)
            participant_per_test = participation_record.get_participant_per_test_for_uid(participant_per_test_uid)

            # Check if the user is logged in
            usr = Member.current()

            if not usr or (not usr.is_admin() and usr.key != participant_per_test.member):
                Member.show_error_unrecognized_usr(self)
                return

            participation_record.remove_member_test_for_uid(participant_per_test_uid)
            participation_record.put()
            time.sleep(1)

            if org == "admin" and usr.is_admin():
                return_address = "/participation_record/modify?id="
            else:
                return_address = "/member/participation_record?id="

            return self.redirect(return_address + participation_record.key.urlsafe())
        except Exception as e:
            logging.error("Deleting member-test in participation_record", str(e))
            return self.redirect("/error?msg=Deleting member-test in participation record: " + str(e))


app = webapp2.WSGIApplication([
    ("/participation_record/participant_per_test/delete", DeleteMemberTestForParticipationRecordHandler),
], debug=True)
