#!/usr/bin/python3
'''defin read_file dunction'''


def read_file(filename=""):
    '''Reads a file 'utf-8' and prints it.'''
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
