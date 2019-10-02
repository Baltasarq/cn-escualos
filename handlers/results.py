#!/usr/bin/env python
# coding: utf-8
# CnEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member
from model.document import Document


class ResultsHandler(webapp2.RequestHandler):
    RESULT_KEYWORDS = [
        "clasificacion",
        "clasificación",
        "clasificaciones",
        "resultados"
    ]

    def filter_by_results(self, document):
        for tag in document.tags:
            tag = tag.lower()
            if tag in ResultsHandler.RESULT_KEYWORDS:
                self.result_documents.append(document)
                break

        return

    def get(self):
        try:
            # Get current user (though not mandatory)
            usr = Member.current()

            # Retrieve relevant documents
            self.result_documents = []
            Document.query().order(-Document.added).map(self.filter_by_results)

            # Render
            template_values = {
                "usr": Member.current(),
                "info": AppInfo,
                "result_documents": self.result_documents
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("results.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ("/results", ResultsHandler),
], debug=True)
