#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016/19 MIT License <baltasarq@gmail.com>


import webapp2
from google.appengine.ext import ndb

from model.photo import Photo


class PhotoServerHandler(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET["id"]
        except KeyError:
            self.redirect("/error?msg='missing id for photo'")
            return

        # Retrieve the photo from the datastore
        image_object = ndb.Key(urlsafe=id).get()

        if not image_object:
            self.redirect("/error?msg='photo not found with id: ' + id")
            return

        # Return the requested document
        self.response.headers['Content-Type'] = "image/jpg"
        self.response.out.write(image_object.image)


app = webapp2.WSGIApplication([
    ('/photoserver', PhotoServerHandler)
], debug=True)
