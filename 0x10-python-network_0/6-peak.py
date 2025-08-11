#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak element in the list using a binary search approach.
    Returns None if the list is empty.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare mid element with its right neighbor
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Peak must be in the right half
            left = mid + 1
        else:
            # Peak is in the left half (including mid)
            right = mid

    # At the end, left == right, the peak element
    return list_of_integers[left]
