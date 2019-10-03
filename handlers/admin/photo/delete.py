#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Delete photos


import time
import logging
import webapp2
from google.appengine.ext import ndb

from model.member import Member


class DeletePhotosHandler(webapp2.RequestHandler):
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
            logging.error("deleting photo", str(e))
            return self.redirect("/error?msg=No id of photo to delete")

        try:
            ndb.Key(urlsafe=id).delete()
            time.sleep(1)
        except:
            return self.redirect("/error?msg=key #" + str(id) + " does not exist")

        return self.redirect("/admin/photos")


app = webapp2.WSGIApplication([
    ("/admin/photo/delete", DeletePhotosHandler),
], debug=True)
