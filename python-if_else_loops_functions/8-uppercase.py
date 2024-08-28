#!/usr/bin/python3
#Write a function that prints a string in uppercase followed by a new line.
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 123:
            print('{}'.format(chr(ord(i)-32)), end="")
        else:
            print('{}'.format(i), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")