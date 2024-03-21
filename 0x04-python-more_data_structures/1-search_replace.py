#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == e else e for e in my_list]
