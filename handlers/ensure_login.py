#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from model.member import Member


class EnsureLoginHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.retrieve_usr_data()
        if not usr:
            gae_usr = users.get_current_user()

            if not users.is_current_user_admin():
                self.redirect("/error?msg=Unregistered user: " + gae_usr.email())
                return
            else:
                usr = Member.current()

        try:
            if usr.identified:
                gae_usr = users.get_current_user()
                self.response.write(gae_usr.nickname() + " already identified, redirecting to personal page.")
                self.redirect("/member/modify")
                return
            else:
                data = {
                    "usr": usr
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("ensure_login.html", **data))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))

    def post(self):
        usr_dni = self.request.get("edDni", "0")
        usr_soc = self.request.get("edSoc", "0")

        # Check if the user is logged in
        gae_usr = users.get_current_user()

        if not gae_usr:
            self.redirect("/error?msg=User not logged in.")

        # Retrieve the user info from the data store
        usr = None
        list_usrs_found = Member.query(Member.user_id == gae_usr.user_id()).fetch()

        if (list_usrs_found
        and len(list_usrs_found) > 0):
            usr = list_usrs_found[0]

        if (usr_soc
        and usr_dni
        and usr.soc.strip().lower() == usr_soc.strip().lower()
        and usr.dni.strip().lower() == usr_dni.strip().lower()):
            usr.identified = True
            usr.put()
            self.redirect("/member")
        else:
            self.redirect("/error?msg=Usuario "
                                + usr_dni
                                + " #" + usr_soc
                                + " no reconocido como miembro del club.")


app = webapp2.WSGIApplication([
    ("/ensure_login", EnsureLoginHandler),
], debug=True)
