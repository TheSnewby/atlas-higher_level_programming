#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    if x == 0:
        return printed
    for item in my_list:
        try:
            print('{}'.format(item), end='')
        except IndexError:
            break
        printed += 1
        if printed == x:
            break
    print()
    return printed
