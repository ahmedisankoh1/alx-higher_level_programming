#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    i = x

    for item in range(i):
        try:
            print(f"{my_list[item]}", end="")
            count += 1
        except IndexError:
            break
    print()
    return (count)
