#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 123:
            print('{}'.format(chr(ord(i + 32))), end="")
        else:
            print('{}'.format(i), end="")
