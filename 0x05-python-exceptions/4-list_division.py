#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_div = []
    try:
        for i in range(list_length):
            try:
                list_div.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                list_div.append(0)
                print("division by 0")
                continue
            except TypeError:
                list_div.append(0)
                print("wrong type")
                continue
            except IndexError:
                list_div.append(0)
                print("out of range")
                continue
            finally:
                pass

        return list_div
