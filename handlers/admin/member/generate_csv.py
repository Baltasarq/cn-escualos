#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Generates members list as CSV


import webapp2
from webapp2_extras import jinja2

from model.member import Member


class GenerateMembersCSVHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "members": Member.query().order(Member.surname).order(Member.name).fetch()
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.headers['Content-Type'] = "text/csv"
        self.response.headers['Content-Disposition'] = "attachment; filename=cnescualos-members.csv"
        self.response.write(jinja.render_template("member_data.csv", **template_values))
        return


app = webapp2.WSGIApplication([
    ("/admin/member/generate_csv", GenerateMembersCSVHandler),
], debug=True)
