#!/usr/bin/python3
''' Module for lookup method'''


def lookup(obj):
    '''Looks up for objects attributes and methods.
    Args:
        obj (object): the object to list.

    Return:
        list: the list of attributes and methods.
    '''
    return dir(obj)
