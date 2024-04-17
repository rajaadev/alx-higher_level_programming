#!/usr/bin/python3
'''Define write_file with two arguments'''


def write_file(filename="", text=""):
    '''Writes a file with UTF-8.'''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
