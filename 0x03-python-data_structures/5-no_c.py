#!/usr/bin/python3

def no_c(my_string):
    char_to_remove = "cC"
    new_string = ''.join(char for char in my_string if char not in char_to_remove)
    return (new_string)

