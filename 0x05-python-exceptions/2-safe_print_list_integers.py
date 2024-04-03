#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    while i < x:
    try:
        print("{:d}".format(my_list[item]), end="")
        counter = counter + 1
    except (ValueError, TypeError):
        pass
    item += 1
    print()
    return (counter)
