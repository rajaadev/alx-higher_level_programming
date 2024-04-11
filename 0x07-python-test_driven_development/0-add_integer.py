#!/usr/bin/python3
"""Define two integers or float casted to integer addition function casted."""


def add_integer(a, b=98):
 """Return the integer addition of a and b"""

 if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.doctest.testfile("tests/0-add_integer.txt")
