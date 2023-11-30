#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    result = 0

    arg_len = len(sys.argv) - 1
    if arg_len == 0 or arg_len == 1:
        print("0")
    elif arg_len > 1:
        for check in range(arg_len):
            result = result + int(sys.argv[check + 1])   
        print("{}".format(result))
