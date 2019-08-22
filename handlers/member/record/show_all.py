#!/usr/bin/env python
# (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.member import Member
from model.appinfo import AppInfo
from model.record_entry import RecordEntry
from model.record_entry import SwimStyles


class Record:
    def __init__(self, dni, surname, name, record_entry):
        self.added = record_entry.added
        self.dni = dni
        self.name = name
        self.surname = surname
        self.distance = record_entry.distance
        self.style = SwimStyles.name_from_id(record_entry.style_id)
        self.millis = record_entry.milliseconds
        self.where = record_entry.where

    def sorting_key(self):
        return (self.distance * 10) + self.millis

    def str_from_milliseconds(self):
        return RecordEntry.str_from_milliseconds(self.millis)

    def __str__(self):
        return str(self.added) + ' ' + self.surname \
                + ", " + self.name + ": " + self.distance + "m " \
                + self.str_from_milliseconds() \
                + " @ " + self.where


class ShowAllRecordsHandler(webapp2.RequestHandler):
    def get(self):
        try:
            records_per_distance = {}
            members = Member.query()

            # Get current user, but anyway this section is public
            usr = Member.retrieve_usr_data()

            # Collect all data
            for m in members:
                for record_entry in m.records:
                    distance = record_entry.distance
                    records_list = records_per_distance.get(distance)

                    if not records_list:
                        records_list = []
                        records_per_distance[distance] = records_list

                    records_list.append(Record(
                        m.dni,
                        m.surname,
                        m.name,
                        record_entry))

            # Sort data
            distances = records_per_distance.keys()
            distances.sort()

            for pair in records_per_distance.items():
                pair[1].sort(key=lambda r: r.sorting_key())

            template_values = {
                "info": AppInfo,
                "usr": usr,
                "distances": distances,
                "records_per_distance": records_per_distance,
            }

            # Render answer
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("records.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ("/member/record/show_all", ShowAllRecordsHandler),
], debug=True)
