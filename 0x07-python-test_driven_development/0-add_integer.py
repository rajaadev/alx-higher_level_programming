#!/usr/bin/python3
"""Define two integers or float addition function."""


def add_integer(a, b=98):
	""" add twi integers or floats a and b """
	if not isinstance(a, (int, float)):
		raise TypeError("a must be an integer")
	if not isinstance(b, (int, float)): 
		raise TypeError("b must be an integer")
	return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
