#!/usr/bin/python3

def remove_char_at(str, n):
    str_cp = (str[0:n] + str[n+1:])
    
    if n < 0:
        return (str)
    return (str_cp)
