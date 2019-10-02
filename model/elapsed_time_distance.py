#!/usr/bin/env python
# CNEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb


class ElapsedTimeDistance(ndb.Model):
    style_id = ndb.IntegerProperty(required=True, indexed=True)
    distance = ndb.IntegerProperty(required=True, indexed=True)
    milliseconds = ndb.IntegerProperty(required=True, indexed=True)

    @staticmethod
    def total_seconds(millis):
        return millis // 1000

    @staticmethod
    def part_millis(millis):
        return millis % 1000

    @staticmethod
    def part_seconds(millis):
        toret = ElapsedTimeDistance.total_seconds(millis)

        # Remove hours
        toret %= 3600

        # Remove minutes
        toret %= 60

        return toret

    @staticmethod
    def part_minutes(millis):
        toret = ElapsedTimeDistance.total_seconds(millis)

        # Remove hours
        toret %= 3600

        # Remove minutes
        return toret // 60

    @staticmethod
    def part_hours(millis):
        toret = ElapsedTimeDistance.total_seconds(millis)

        # Remove hours
        return toret // 3600

    @staticmethod
    def str_from_milliseconds(millis):
        return str.format("{0:02d}h {1:02d}' {2:02d}\" {3:03d}ms",
                          ElapsedTimeDistance.part_hours(millis),
                          ElapsedTimeDistance.part_minutes(millis),
                          ElapsedTimeDistance.part_seconds(millis),
                          ElapsedTimeDistance.part_millis(millis))

    @staticmethod
    def millis_from_parts(h, m, s, ms):
        return (h * 3600000) + (m * 60000) + (s * 1000) + ms

    def __str__(self):
        return ElapsedTimeDistance.str_from_milliseconds(self.milliseconds)
