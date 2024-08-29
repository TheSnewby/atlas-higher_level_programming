#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print('{} argument'.format(len(sys.argv) - 1), end='')
    if len(sys.argv) - 1 == 0:
        print('s.')
    elif len(sys.argv) - 1 == 1:
        print(':')
    else:
        print('s:')
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
