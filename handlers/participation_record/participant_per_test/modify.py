#!/usr/bin/env python
# coding: utf-8
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging

import webapp2
from google.appengine.ext import ndb

from model.member import Member
from model.elapsed_time_distance import ElapsedTimeDistance
from model.participation_record import ParticipationRecord
from model.participation_record import MemberTest


class ModifyMemberPerTestForParticipationRecordHandler(webapp2.RequestHandler):
    def post(self):
        try:
            # Establish the origin
            org = self.request.GET.get("org")

            if not org:
                org = "admin"

            # Assign data to this member per test
            participation_record = ParticipationRecord.retrieve_participation_record(self)

            str_member_key = self.request.get("edMemberPerTest", "")
            str_test_uid = self.request.get("edTest", "")
            str_hours = self.request.get("edHours", "0")
            str_minutes = self.request.get("edMinutes", "0")
            str_seconds = self.request.get("edSeconds", "0")
            str_millis = self.request.get("edMillis", "0")

            if str_member_key and str_test_uid:
                member_key = ndb.Key(urlsafe=str_member_key)

                # Check if the user is logged in
                usr = Member.current()

                if not usr or (not usr.is_admin() and member_key != usr.key):
                    Member.show_error_unrecognized_usr(self)
                    return

                # Go on
                competition = participation_record.competition.get()

                # Test uid
                try:
                    test_uid = int(str_test_uid)
                except ValueError:
                    return self.redirect("/error?msg=incorrect test id: '" + str_test_uid + "'")
                
                test = competition.look_for_test_with_uid(test_uid)
                if not test:
                    return self.redirect("/error?msg=test not found for id: '" + str_test_uid + "'")

                try:
                    hours = int(str_hours)
                    minutes = int(str_minutes)
                    seconds = int(str_seconds)
                    millis = int(str_millis)
                except ValueError:
                    return self.redirect("/error?msg=Incorrect record: "
                                         + str.format("{:02d}h {:02d}' {:02d}\" {:02d}ms"))

                millis = ElapsedTimeDistance.millis_from_parts(hours, minutes, seconds, millis)
                member_test = participation_record.get_participant_per_test(member_key, test_uid)

                if not member_test:
                    member_test = MemberTest(
                        member=member_key,
                        test_uid=test_uid,
                        milliseconds=millis)
                    participation_record.add_participant_per_test(member_test)
                else:
                    member_test.milliseconds = millis

                participation_record.put()
                time.sleep(1)
                return_addr = "/member/participation_record?id="

                if org == "admin" and usr.is_admin():
                    return_addr = "/participation_record/modify?id="

                return self.redirect(return_addr + participation_record.key.urlsafe())
            else:
                return self.redirect("/error?msg=Not enough data storing member per test participation.")
        except Exception as e:
            logging.error("Storing member per test in participation_record", str(e))
            return self.redirect("/error?msg=Storing member per test in participation record: " + str(e))


app = webapp2.WSGIApplication([
    ("/participation_record/participant_per_test/modify", ModifyMemberPerTestForParticipationRecordHandler),
], debug=True)
