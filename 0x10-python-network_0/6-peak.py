#!/usr/bin/python3
"""Find the peak in an array"""

def FindAPeak(arr, i, j):
    """Binary Search"""
    mid = int((i + j) / 2)
    # if mid element is peak
    if (mid == len(arr)-1 or arr[mid] >= arr[mid+1]) and (mid == 0 or arr[mid] >= arr[mid-1]):
        return arr[mid]

    if arr[mid] < arr[mid+1] and mid+1 < len(arr):
        return FindAPeak(arr, mid+1, j)
    else:
        return FindAPeak(arr, i, mid-1)
        
def find_peak(list_of_integers):
    """Pass the list"""

    l = list_of_integers

    if len(l) == 0:
        return None

    peak = FindAPeak(l, 0, len(l) - 1)
    return peak
