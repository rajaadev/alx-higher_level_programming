#!/usr/bin/python3
'''defin from_json_string.'''


def from_json_string(my_str):
    '''Returns an object (Python data structure) represented by a JSON string.'''

    
    def parse_value(token):
        if token == 'true':
            return True
        elif token == 'false':
            return False
        elif token.isdigit():
            return int(token)
        elif '.' in token:
            return float(token)
        elif token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        elif token.startswith('['):
            return parse_array(token)
        elif token.startswith('{'):
            return parse_object(token)
        else:
            raise ValueError(f"Unexpected token: {token}")

    def parse_array(array_str):
        elements = array_str[1:-1].split(', ')
        return [parse_value(token) for token in elements]

    def parse_object(object_str):
        pairs = object_str[1:-1].split(', ')
        obj = {}
        for pair in pairs:
            key, value = pair.split(': ')
            obj[key[1:-1]] = parse_value(value)
        return obj
    return parse_value(my_str)
