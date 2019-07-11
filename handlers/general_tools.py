#!/usr/bin/env python
# CNEscualos (c) Baltasar 2016-19 MIT License <baltasarq@gmail.com>
# Generic tools


import traceback


def int_from_str(s):
    """Converts a string into an integer.

        :param s: The string to convert into an integer.
    """
    toret = 0

    if (s
    and s.strip()):
        s = s.strip()

        try:
            toret = int(s)
        except ValueError:
            toret = 0

    return toret


def error_from_exception(e):
    """Returns a meaningful error message from an exception.
    
        :param e: The exception to convert.
    """
    return "<b>" + type(e).__name__ + ": " + str(e) + "</b>" \
           + "<p>" + str.join("<br/>", (traceback.format_list(traceback.extract_stack()))) + "</p>"
