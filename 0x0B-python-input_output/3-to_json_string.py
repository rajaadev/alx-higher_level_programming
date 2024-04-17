#!/usr/bin/python3
'''defin to jason_string function'''


def to_json_string(my_obj):
    '''Returns the JSON representation of an object (string).'''
    if isinstance(my_obj, str):
        return '"' + my_obj + '"'
    elif isinstance(my_obj, (int, float, bool)):
        return str(my_obj).lower()
    elif isinstance(my_obj, (list, tuple)):
        items = ', '.join(to_json_string(item) for item in my_obj)
        return '[' + items + ']'
    elif isinstance(my_obj, dict):
        pairs = ', '.join(f'"{key}": {to_json_string(value)}'\
		for key, value in my_obj.items())
        return '{' + pairs + '}'
    else:
        raise TypeError(f"{my_obj} is not JSON serializable")
