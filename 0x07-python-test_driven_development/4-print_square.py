#!/usr/bin/python3
"""module for print_square method."""


def print_square(size):
    """Prints a square with # characters.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float and less than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
