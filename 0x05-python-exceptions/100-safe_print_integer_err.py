#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    is_integer = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (is_integer)
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        is_integer = False
        return (is_integer)
