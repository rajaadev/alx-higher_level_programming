#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result_div = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result_div = None
    finally:
        print("Inside result: {}".format(result_div))
    return (result_div)
