#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

import handlers.general_tools as gentools
from model.member import Member
from model.swim_styles import SwimStyles
from model.appinfo import AppInfo


class ModifyMemberHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()
        if not usr:
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # User info
            data = {
                "info": AppInfo,
                "usr": usr,
                "SwimStyles": SwimStyles,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("user.html", **data))
        except Exception as e:
            logging.error("ERROR: " + gentools.error_from_exception(e))
            self.response.write("ERROR: " + gentools.error_from_exception(e))

    def post(self):
        # Check if the user is logged in
        usr = Member.current()

        if not usr:
            Member.show_error_unrecognized_usr(self)
            return

        try:
            Member.assign_data(usr, self.request)
        except Exception as e:
            logging.error("Storing usr", str(e))
            return self.redirect("/error?msg=Storing usr: " + str(e))

        # Send a response
        self.redirect("/member/modify")
        return


app = webapp2.WSGIApplication([
    ("/member/modify", ModifyMemberHandler),
], debug=True)
