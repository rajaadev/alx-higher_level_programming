#!/usr/bin/python3
'''Module for MyList class.'''


class MyList(list):
    '''MyList class.'''
    
    def print_sorted(self):
        """
        Method prints sorted list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
