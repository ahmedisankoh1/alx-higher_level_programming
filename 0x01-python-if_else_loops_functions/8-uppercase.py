#!/usr/bin/python3

def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            c = chr(ord(a) - 32)
        print("{}".format(a), end="")
    print("")
