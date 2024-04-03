#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result_div = a / b
    except ZeroDivisionError:
        result_div = None
    finally:
        print("Inside result: {}".format(result))
    return (result_div)
