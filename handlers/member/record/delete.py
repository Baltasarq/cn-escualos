#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Delete record


import time
import logging
import webapp2

from model.member import Member
import handlers.general_tools as tools


class DeleteRecordHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # Get current user, mandatory
            usr = Member.current()

            # Render ack
            if usr:
                # Retrieve record data
                try:
                    str_record_index = self.request.GET["id"]
                except KeyError:
                    return self.redirect("/error?msg=Record entry index was not given")

                record_index = tools.int_from_str(str_record_index) -1
                del usr.records[record_index]
                usr.put()
                time.sleep(1)
                return self.redirect("/member/modify")
            else:
                return Member.show_error_unrecognized_usr(self)
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/member/record/delete', DeleteRecordHandler)
], debug=True)
