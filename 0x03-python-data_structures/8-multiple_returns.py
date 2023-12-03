#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len < 1:
        return (None)
    else:
        first_char = sentence[0]
        ret_value = (str_len, first_char)
        return (ret_value)
