#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    len_list = len(my_list)
    if idx >= len_list:
        return (my_list)
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return (new_list)
