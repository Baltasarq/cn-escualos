#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import time
import logging

import webapp2

from model.member import Member
from model.competition import Competition


class DeleteTestCompetitionHandler(webapp2.RequestHandler):
    def get(self):
        # Check if the user is logged in
        usr = Member.current()

        if not usr or not usr.is_admin():
            Member.show_error_unrecognized_usr(self)
            return

        try:
            # Retrieve competition
            competition = Competition.retrieve_competition(self)

            # Retrieve test uid
            str_test_uid = self.request.GET.get("test_id")
            test_uid = 0

            if str_test_uid:
                try:
                    test_uid = int(str_test_uid)
                except ValueError:
                    error_msg = "Deleting test: converting test uid: '" + str_test_uid + "'"
                    logging.error(error_msg)
                    return self.redirect("/error?msg=" + error_msg)

                competition.delete_test_with_uid(test_uid)
                competition.put()
                time.sleep(1)
                return self.redirect("/competition/modify?id=" + competition.key.urlsafe())
            else:
                return self.redirect("/error?msg=Not enough data deleting test in competition.")
        except Exception as e:
            logging.error("Deleting test in competition", str(e))
            return self.redirect("/error?msg=Deleting test in competition: " + str(e))


app = webapp2.WSGIApplication([
    ("/competition/test/delete", DeleteTestCompetitionHandler),
], debug=True)
