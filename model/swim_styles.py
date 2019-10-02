#!/usr/bin/env python
# CNEscualos (c) baltasar 2016/19 MIT License <baltasarq@gmail.com>


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
