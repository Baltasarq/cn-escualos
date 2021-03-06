#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Add record


import logging
import time
import webapp2

from model.member import Member
from model.swim_styles import SwimStyles
from model.record_entry import RecordEntry
from model.elapsed_time_distance import ElapsedTimeDistance
import handlers.general_tools as tools


class AddRecordHandler(webapp2.RequestHandler):
    def post(self):
        try:
            # Get current user, mandatory
            usr = Member.current()

            # Render ack
            if usr:
                # Retrieve record data
                where = self.request.get("edWhere", "").strip().lower().capitalize()
                distance = tools.int_from_str(self.request.get("edDistance", "0"))
                hours = tools.int_from_str(self.request.get("edHours", "0"))
                minutes = tools.int_from_str(self.request.get("edMinutes", "0"))
                seconds = tools.int_from_str(self.request.get("edSeconds", "10"))
                milliseconds = tools.int_from_str(self.request.get("edMillis", "0"))
                style_abbrev = self.request.get("edStyle", "crl")
                style_id = SwimStyles.id_from_abbrev(style_abbrev)

                rcrd = RecordEntry(
                            where=where,
                            style_id=style_id,
                            distance=distance,
                            milliseconds=ElapsedTimeDistance.millis_from_parts(hours, minutes, seconds, milliseconds))
                usr.records.append(rcrd)
                usr.put()
                time.sleep(1)
                return self.redirect("/member/modify")
            else:
                return Member.show_error_unrecognized_usr(self)
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ('/member/record/add', AddRecordHandler)
], debug=True)
