#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    item, counter = 0, 0
    try:
        for item in my_list:
            if counter < x and isinstance(item, int):
                print("{:d}".format(my_list[item]), end="")
                    counter = counter + 1
    except IndexError:
        pass
    print()
    return (counter)
