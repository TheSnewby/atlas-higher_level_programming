#!/usr/bin/python3
# Write a function that outputs a string in uppercase followed by a new line.
def uppercase(str):
    for i in str:
        print(('{}'.format(chr(ord(i)-32)) if 97 <= ord(i) <= 123 else
               '{}'.format(i)), end="")
    print()
