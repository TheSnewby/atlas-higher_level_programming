#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print('{} arguments'.format(len(sys.argv) - 1), end='')
    print('{}'.format('.' if len(sys.argv) - 1 == 0 else ':'))
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
