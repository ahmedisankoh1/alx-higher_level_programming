#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keyes = list(a_dictionary.keys())
    keyes.sort()
    for key in keyes:
        print("{}: {}".format(key, a_dictionary[key]))
