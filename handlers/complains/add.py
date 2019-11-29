#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Add complain


import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member
from model.complaint import Complaint


class AddComplainHandler(webapp2.RequestHandler):
    def get(self):
        usr = Member.current()

        if not usr:
            return self.redirect("/error?msg=You must be a member.")

        # Render answer
        template_values = {
            "info": AppInfo,
            "usr": usr,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("add_complain.html", **template_values))

    def post(self):
        usr = Member.current()

        if not usr:
            return self.redirect("/error?msg=You must be a member.")

        complain_text = self.request.get("edComplain", "").strip()

        if not complain_text:
            return self.redirect("/error?msg=El mensaje de sugerencia no es significativo.")

        complain = Complaint(author=usr.key, text=complain_text)
        complain.put()
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/complains/add', AddComplainHandler)
], debug=True)
