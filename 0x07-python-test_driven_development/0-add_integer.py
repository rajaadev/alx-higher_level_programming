
#!/usr/bin/python3
"""Define two integers or float addition function."""


def add_integer(a, b=98):
	""" add twi integers or floats a and b """
	if type (a) and not in(int, float):
		raise TypeError("a must be an integer ")
	if type (b) and not in(int, float): 
		raise TypeError("b must be an integer ")
return (int(a) + int(b))
