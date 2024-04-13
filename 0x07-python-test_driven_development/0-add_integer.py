#!/usr/bin/python3
"""Module defin add_integer function."""


def add_integer(a, b=98):
	"""add two integers or floats
	Args:
		a: first number.
		b: second number, default 98.
	Raises:
		TypeError: if a, b are not int, float.
	Return:
		The sum of the two integers.
	"""

	if not isinstance(a, (int, float)):
		raise TypeError("a must be an integer")
	if not isinstance(b, (int, float)): 
		raise TypeError("b must be an integer")
	return (int(a) + int(b))


if __name__ == "__main__":
	import doctest
	doctest.testfile("tests/0-add_integer.txt")
