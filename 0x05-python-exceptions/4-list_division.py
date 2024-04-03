#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_div = []
    for i in range(list_length):
        try:
            result_div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            continue
            result_div = 0
        except TypeError:
            print("wrong type")
            result_div = 0
            continue
        except IndexError:
            print("out of range")
            result_div = 0
            continue
        finally:
            list_div.append(result_div)
    return list_div
