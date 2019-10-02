#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Delete members


import time
import logging
import webapp2
from google.appengine.ext import ndb

from model.member import Member


class DeleteMemberHandler(webapp2.RequestHandler):
    def get(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not usr.is_admin()):
            return Member.show_error_unrecognized_usr(self)

        # Get the data
        id = None
        try:
            id = self.request.GET["id"]
        except KeyError as e:
            logging.error("deleting member", str(e))
            return self.redirect("/error?msg=No id of member to delete")

        try:
            ndb.Key(urlsafe=id).delete()
            time.sleep(1)
        except:
            return self.redirect("/error?msg=key #" + str(id) + " does not exist")

        return self.redirect("/admin/members")


app = webapp2.WSGIApplication([
    ("/admin/member/delete", DeleteMemberHandler),
], debug=True)
