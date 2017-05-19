#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.document import Document


class PhotosHandler(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET["id"]
        except KeyError:
            self.redirect("/error?msg='missing id for document'")
            return

        # Retrieve the document from the datastore
        doc = ndb.Key(urlsafe=id).get()

        if not doc:
            self.redirect("/error?msg='document not found with id: ' + id")
            return

        # Return the requested document
        self.response.headers['Content-Type'] = "application/pdf"
        self.response.headers['Content-Disposition'] = "attachment; filename=cnescualos-doc-" + id.encode('ascii','ignore') + ".pdf"
        self.response.out.write(doc.file)


app = webapp2.WSGIApplication([
    ('/docserver', PhotosHandler)
], debug=True)
