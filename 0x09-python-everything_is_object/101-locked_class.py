#!/usr/bin/python3
"""Module defining LockedClass which restricts instance attributes."""

class LockedClass:
    """Class that only allows an instance attribute called 'first_name'.

    Prevents dynamically creating any other instance attributes.
    """
    __slots__ = ['first_name']
