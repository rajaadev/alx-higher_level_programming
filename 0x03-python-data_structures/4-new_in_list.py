#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx not in range(len(my_list)):
        return my_list.cpy()
    else:
        my_list1 = my_list.copy()
        my_list1[idx] = element
    return my_list1
