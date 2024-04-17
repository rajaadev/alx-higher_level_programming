#!/usr/bin/python3
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item_to_list(filename, *items):
    '''Adds items to a list and saves it to a file.'''
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(items)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item_to_list("add_item.json", *sys.argv[1:])
