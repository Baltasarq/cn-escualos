#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016/19 MIT License <baltasarq@gmail.com>


import webapp2
from google.appengine.ext import ndb


class RetrievePaymentHandler(webapp2.RequestHandler):
    def get(self):
        # Retrieve the payment id
        try:
            str_payment_id = self.request.GET["id"]
        except KeyError:
            self.redirect("/error?msg='missing payment id in participation record'")
            return

        payment = ndb.Key(urlsafe=str_payment_id).get().payment

        # Return the requested document
        self.response.headers['Content-Type'] = "application/pdf"
        self.response.headers['Content-Disposition'] = "attachment; filename=cnescualos-resguardo-" + str_payment_id.encode('ascii','ignore') + ".pdf"
        self.response.out.write(payment)


app = webapp2.WSGIApplication([
    ('/participation_record/member_participation/retrieve_payment', RetrievePaymentHandler)
], debug=True)
