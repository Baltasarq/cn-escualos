#!/usr/bin/env python
# MIT License
# (c) baltasar 2016

import webapp2
from webapp2_extras.users import users

from model.member import Member


class EnsureLoginHandler(webapp2.RequestHandler):
    def get(self):
        usr = Member.current()

        if not usr:
            if users.is_current_user_admin():
                Member.set_admin()
            else:
                return Member.show_error_unrecognized_usr(self)

        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/ensure_login', EnsureLoginHandler)
], debug=True)
