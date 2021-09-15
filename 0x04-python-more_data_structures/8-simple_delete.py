#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    for k in a_dictionary:
        if k is key:
           del a_dictionary[k]
    return a_dictionary
