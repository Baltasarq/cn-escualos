#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.appinfo import AppInfo
from model.document import Document


class DocsHandler(webapp2.RequestHandler):
    def get(self):
        try:
            tags = self.request.GET["tags"]
        except KeyError:
            tags = None

        if not tags:
            documents = Document.query().order(-Document.added)
        else:
            tags = tags.split(',')
            for tag in tags:
                documents = Document.query(tag in Document.tags)

        template_values = {
            "info": AppInfo,
            "documents": documents,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("docs.html", **template_values))

app = webapp2.WSGIApplication([
    ('/docs', DocsHandler)
], debug=True)
