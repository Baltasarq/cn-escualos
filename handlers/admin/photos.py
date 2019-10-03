#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Photos


import time
import logging
import webapp2
from google.appengine.api import images
from webapp2_extras import jinja2
from datetime import datetime

from model.appinfo import AppInfo
from model.photo import Photo
from model.member import Member


class PhotosHandler(webapp2.RequestHandler):
    def get(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not usr.is_admin()):
            return Member.show_error_unrecognized_usr(self)

        # Render trials
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "photos": Photo.query().order(-Photo.added).fetch()
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("kernel_photos.html", **template_values));
        except Exception as e:
            logging.error("rendering trials", str(e))
            self.response.write("ERROR: " + str(e))

    def post(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not (usr.is_admin())):
            return Member.show_error_unrecognized_usr(self)

        # Get the data
        title = self.request.get("edTitle", "").strip()
        tags = self.request.get("edTags", "").strip().split(',')

        if not title:
            return self.redirect("/error?msg=Foto sin titulo")

        image = None
        try:
            image_data = self.request.get("edImage", None)

            if image_data:
                image = images.Image(image_data)
                width = image.width
                height = image.height
                new_width = (400 * width) / height
                image = images.resize(image_data, new_width, 400)
        except images.Error as e:
            logging.error("Getting image", str(e))

        photo = Photo(title=title, tags=tags)
        if image:
            photo.image = image

        photo.put()
        time.sleep(1)
        return self.redirect("/admin/photos")


app = webapp2.WSGIApplication([
    ("/admin/photos", PhotosHandler),
], debug=True)
