#!/usr/bin/env python
# coding: utf-8
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging

import webapp2
from google.appengine.ext import ndb

from model.member import Member
from model.participation_record import ParticipationRecord
from model.participation_record import MemberParticipation


class ModifyMemberParticipationForParticipationRecordHandler(webapp2.RequestHandler):
    def post(self):
        try:
            # State org
            org = self.request.GET.get("org")

            if not org:
                org = "admin"

            # Assign data to this competition
            participation_record = ParticipationRecord.retrieve_participation_record(self)

            member_key = self.request.get("edMember", "")
            str_stays_for_lunch = self.request.get("edLunch", "off")
            payment_blob = self.request.get("edPayment", None)
            comments = self.request.get("edComments", "").strip()
            str_companions = self.request.get("edCompanions", "0")

            try:
                num_companions = int(str_companions)
            except ValueError:
                num_companions = 0

            if member_key:
                member_key = ndb.Key(urlsafe=member_key)

                # Check if the user is logged in
                usr = Member.current()

                if not usr or (not usr.is_admin() and usr.key != member_key):
                    Member.show_error_unrecognized_usr(self)
                    return

                member_participation = participation_record.get_participant_info(member_key)

                if not member_participation:
                    member_participation = MemberParticipation()
                    member_participation.member = member_key
                    participation_record.participants.append(member_participation)

                member_participation.stays_for_lunch = (str_stays_for_lunch == "on")
                member_participation.num_companions = num_companions

                if payment_blob:
                    member_participation.payment = payment_blob

                if comments:
                    if comments == "-":
                        member_participation.comments = ""
                    else:
                        member_participation.comments = comments

                participation_record.put()
                time.sleep(1)

                return_addr = "/member/participation_record?id="
                if org == "admin" and usr.is_admin():
                    return_addr = "/participation_record/modify?id="

                return self.redirect(return_addr + participation_record.key.urlsafe())
            else:
                return self.redirect("/error?msg=Not enough data storing member participation.")
        except Exception as e:
            logging.error("Storing member participation in participation_record", str(e))
            return self.redirect("/error?msg=Storing member participation in participation record: " + str(e))


app = webapp2.WSGIApplication([
    ("/participation_record/member_participation/modify", ModifyMemberParticipationForParticipationRecordHandler),
], debug=True)
