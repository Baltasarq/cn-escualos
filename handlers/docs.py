#!/usr/bin/env python
# MIT License
# (c) baltasar 2016


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.document import Document
from model.member import Member


class DocsHandler(webapp2.RequestHandler):
    def get(self):
        # Get current user, thought not required
        usr = Member.current()

        # Get the relevant tags
        try:
            tags = self.request.GET["tags"]
        except KeyError:
            tags = None

        # Get the relevant documents
        try:
            if not tags:
                documents = Document.query().order(-Document.added)
            else:
                tags = tags.split(',')
                for tag in tags:
                    documents = Document.query(tag in Document.tags)

            template_values = {
                "usr": usr,
                "info": AppInfo,
                "documents": documents,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("docs.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/docs', DocsHandler)
], debug=True)
