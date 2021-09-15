#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    for k in a_dictionary.keys:
        if k is key:
            a_dictionary.pop(k)
    return a_dictionary
