#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted = [x for x, i in a_dictionary.items() if i == value]
    for x in deleted:
        del a_dictionary[x]
    return a_dictionary
