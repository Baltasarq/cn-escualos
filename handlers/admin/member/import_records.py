#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Import records for members


import logging
import webapp2
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.member import Member
from model.swim_styles import SwimStyles
from handlers.member.record.importing import import_records_csv_file


class ImportRecordsHandler(webapp2.RequestHandler):
    def get(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not usr.is_admin()):
            return Member.show_error_unrecognized_usr(self)

        # Render import records form
        try:
            template_values = {
                "usr": usr,
                "info": AppInfo,
                "SwimStyles": SwimStyles
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("kernel_import_records.html", **template_values));
        except Exception as e:
            logging.error("rendering patreons", str(e))
            self.response.write("ERROR: " + str(e))

    def post(self):
        # Get the usr
        usr = Member.current()

        if (not usr
         or not (usr.is_admin())):
            return Member.show_error_unrecognized_usr(self)

        # Get the data
        csv_records_contents = self.request.get("edCsv", "").strip()

        if csv_records_contents:
            result_summary = import_records_csv_file(csv_records_contents)
            return self.redirect("/info?msg=" + result_summary.replace('\n', ' '))
        else:
            return self.redirect("/error?msg=Missing CSV data.")


app = webapp2.WSGIApplication([
    ("/admin/member/import_records", ImportRecordsHandler),
], debug=True)
