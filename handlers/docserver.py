#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016/19 MIT License <baltasarq@gmail.com>


import webapp2
from google.appengine.ext import ndb

from model.document import Document


class DocServerHandler(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET["id"]
        except KeyError:
            self.redirect("/error?msg='missing id for document'")
            return

        # Retrieve the document from the datastore
        try:
            doc = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/error?msg='error retrieving document with id: \"" + id + "\"'")
            return

        if not doc:
            self.redirect("/error?msg='document not found with id: \"" + id + "\"'")
            return

        # Return the requested document
        self.response.headers['Content-Type'] = "application/pdf"
        self.response.headers['Content-Disposition'] = "attachment; filename=cnescualos-doc-" + id.encode('ascii','ignore') + ".pdf"
        self.response.out.write(doc.file)


app = webapp2.WSGIApplication([
    ('/docserver', DocServerHandler)
], debug=True)
