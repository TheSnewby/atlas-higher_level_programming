#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print('{}'.format(-1 * (abs(number) % 10)))
        return int(f'-{str(number)[-1]}')
    print('{}'.format(number % 10))
    return int(str(number)[-1])
