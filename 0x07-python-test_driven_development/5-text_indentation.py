#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Prints text with 2 new lines after '.?:' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":
        text = (delimiter + "\n\n").join([line.strip(" ") for line in text.split(delimiter)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
