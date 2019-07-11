#!/usr/bin/env python
# CnEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.photo import Photo
from model.member import Member


class PhotosHandler(webapp2.RequestHandler):
    def get(self):
        # Current user, though not required
        usr = Member.current()

        # Tags for limiting the photos
        try:
            tags = self.request.GET["tags"]
        except KeyError:
            tags = None

        # Get the relevant photos
        if not tags:
            photos = Photo.query().order(-Photo.added)
        else:
            tags = tags.split(',')
            for tag in tags:
                photos = Photo.query(tag in Photo.tags)

        # Render
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "photos": photos,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("photos.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.repsonse.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/photos', PhotosHandler)
], debug=True)
