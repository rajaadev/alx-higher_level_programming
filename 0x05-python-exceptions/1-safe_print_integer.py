#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        while counter is not x:
            print(my_list[counter], end="")
            counter = counter + 1
    except IndexError:
        None
    print()
    return (counter)
