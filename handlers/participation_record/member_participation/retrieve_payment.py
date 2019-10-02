#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016/19 MIT License <baltasarq@gmail.com>


import webapp2
from google.appengine.ext import ndb

from model.participation_record import ParticipationRecord


class RetrievePaymentHandler(webapp2.RequestHandler):
    def get(self):
        participation_record = ParticipationRecord.retrieve_participation_record(self)

        # Retrieve the member id
        try:
            str_member_id = self.request.GET["member_id"]
        except KeyError:
            self.redirect("/error?msg='missing member id for payment in participation record'")
            return

        member_id = ndb.Key(urlsafe=str_member_id)
        member_participation = participation_record.get_participant_info(member_id)

        # Return the requested document
        self.response.headers['Content-Type'] = "application/pdf"
        self.response.headers['Content-Disposition'] = "attachment; filename=cnescualos-resguardo-" + str_member_id.encode('ascii','ignore') + ".pdf"
        self.response.out.write(member_participation.payment)


app = webapp2.WSGIApplication([
    ('/participation_record/member_participation/retrieve_payment', RetrievePaymentHandler)
], debug=True)
