#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print('{}'.format((abs(number) % 10)), end="")
        return int(f'{str(number)[-1]}')
    print('{}'.format(number % 10), end="")
    return int(str(number)[-1])
