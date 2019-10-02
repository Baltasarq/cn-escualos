#!/usr/bin/env python
# (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>


import logging
import webapp2
from webapp2_extras import jinja2

from model.member import Member
from model.appinfo import AppInfo
from model.record_entry import RecordEntry
from model.swim_styles import SwimStyles


class Record:
    def __init__(self, added, dni, surname, name, distance, style, millis, where):
        self.added = added
        self.dni = dni
        self.name = name
        self.surname = surname
        self.distance = distance
        self.style = style
        self.millis = millis
        self.where = where

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
            records_per_distance_and_style = {}
            members = Member.query()

            # Get current user, but anyway this section is public
            usr = Member.current()

            # Collect all data
            # Create a dictionary distance -> style -> records_list
            for m in members:
                for record_entry in m.records:
                    style = SwimStyles.name_from_id(record_entry.style_id)
                    distance = record_entry.distance
                    records_dict = records_per_distance_and_style.get(distance)

                    # Retrieve distance dictionary for all styles in that distance
                    if not records_dict:
                        records_dict = {}
                        records_per_distance_and_style[distance] = records_dict

                    # Retrieve records list for that style
                    records_list = records_dict.get(style)
                    if not records_list:
                        records_list = []
                        records_dict[style] = records_list

                    records_list.append(
                        Record(
                            record_entry.added,
                            m.dni,
                            m.surname,
                            m.name,
                            distance,
                            style,
                            record_entry.milliseconds,
                            record_entry.where))

            # Sort data
            distances = list(records_per_distance_and_style.keys())
            distances.sort()

            for pair_distance_styles in records_per_distance_and_style.items():
                for style in pair_distance_styles[1].keys():
                    pair_distance_styles[1][style].sort(key=lambda r: r.sorting_key())

            # Prepare styles info
            styles = []
            for i in range(SwimStyles.count()):
                styles.append(SwimStyles.name_from_id(i))

            styles.sort()

            # Render answer
            template_values = {
                "info": AppInfo,
                "usr": usr,
                "distances": distances,
                "styles": styles,
                "records_per_distance_and_style": records_per_distance_and_style,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("records.html", **template_values))
        except Exception as e:
            logging.error(str(e))
            self.response.write("ERROR: " + str(e))


app = webapp2.WSGIApplication([
    ("/member/record/show_all", ShowAllRecordsHandler),
], debug=True)
