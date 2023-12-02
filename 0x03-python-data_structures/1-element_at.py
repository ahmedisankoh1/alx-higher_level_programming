#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 1:
        return (None)
    len_list = len(my_list)
    if idx >= len_list:
        return (None)
    else:
        element = my_list[idx]
        return (element)
