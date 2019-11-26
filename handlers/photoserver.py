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
            return self.redirect("/error?msg='missing id for photo'")

        # Retrieve the photo from the datastore
        try:
            image_object = ndb.Key(urlsafe=id).get()
        except:
            return self.redirect("/error?msg='error retrieving photo with id: \"" + id + "\"'")

        if not image_object:
            return self.redirect("/error?msg='photo not found with id: \"" + id + "\"'")

        # Return the requested document
        self.response.headers['Content-Type'] = "image/jpg"
        self.response.out.write(image_object.image)


app = webapp2.WSGIApplication([
    ('/photoserver', PhotoServerHandler)
], debug=True)
