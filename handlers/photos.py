#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.appinfo import AppInfo
from model.photo import Photo


class PhotosHandler(webapp2.RequestHandler):
    def get(self):
        try:
            tags = self.request.GET["tags"]
        except KeyError:
            tags = None

        if not tags:
            photos = Photo.query().order(-Photo.added)
        else:
            tags = tags.split(',')
            for tag in tags:
                photos = Photo.query(tag in Photo.tags)

        template_values = {
            "info": AppInfo,
            "photos": photos,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("photos.html", **template_values))

app = webapp2.WSGIApplication([
    ('/photos', PhotosHandler)
], debug=True)
