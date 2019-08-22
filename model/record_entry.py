#!/usr/bin/env python
# CNEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb


class SwimStyles:
    VALUES = [
        ("lbr", "libre"),
        ("crl", "crol"),
        ("esp", "espalda"),
        ("brz", "braza"),
        ("mrps", "mariposa"),
        ("est", "estilos")
    ]

    @staticmethod
    def count():
        return len(SwimStyles.VALUES)

    @staticmethod
    def value_from_id(i):
        return SwimStyles.VALUES[i]

    @staticmethod
    def abbrev_from_value(v):
        return v[0]

    @staticmethod
    def name_from_value(v):
        return v[1]

    @staticmethod
    def abbrev_from_id(i):
        return SwimStyles.abbrev_from_value(SwimStyles.value_from_id(i))

    @staticmethod
    def name_from_id(i):
        return SwimStyles.name_from_value(SwimStyles.value_from_id(i))

    @staticmethod
    def id_from_abbrev(abbrev):
        abbrev = abbrev.strip().lower() if abbrev else ""

        for i, value in enumerate(SwimStyles.VALUES):
            if SwimStyles.abbrev_from_value(value) == abbrev:
                toret = i
                break
        else:
            raise IndexError("while looking for abbreviation in style: '" + abbrev + '\'')

        return toret


class RecordEntry(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    style_id = ndb.IntegerProperty(required=True, indexed=True)
    distance = ndb.IntegerProperty(required=True, indexed=True)
    where = ndb.StringProperty()
    milliseconds = ndb.IntegerProperty(required=True, indexed=True)

    @staticmethod
    def total_seconds(millis):
        return millis // 1000

    @staticmethod
    def part_millis(millis):
        return millis % 1000

    @staticmethod
    def part_seconds(millis):
        toret = RecordEntry.total_seconds(millis)

        # Remove hours
        toret %= 3600

        # Remove minutes
        toret %= 60

        return toret

    @staticmethod
    def part_minutes(millis):
        toret = RecordEntry.total_seconds(millis)

        # Remove hours
        toret %= 3600

        # Remove minutes
        return toret // 60

    @staticmethod
    def part_hours(millis):
        toret = RecordEntry.total_seconds(millis)

        # Remove hours
        return toret // 3600

    @staticmethod
    def str_from_milliseconds(millis):
        return str.format("{0:02d}h {1:02d}' {2:02d}\" {3:03d}ms",
                               RecordEntry.part_hours(millis),
                               RecordEntry.part_minutes(millis),
                               RecordEntry.part_seconds(millis),
                               RecordEntry.part_millis(millis))

    def __str__(self):
        return RecordEntry.str_from_milliseconds(self.milliseconds)
