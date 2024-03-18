#!/usr/bin/python3
def element_at(my_list, index):
    if index < 0 or  index >= len(my_list):
        return None
    return my_list[index]
