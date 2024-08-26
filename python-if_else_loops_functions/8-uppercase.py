#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 123:
            print(chr(ord(i + 32)), end="")
        else:
            print(i, end="")
