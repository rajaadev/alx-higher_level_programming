def class_to_json(obj):
    '''Returns the dictionary description for JSON serialization of an object.'''
    result = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            result[attr] = value
    return result
