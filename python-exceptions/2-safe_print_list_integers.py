#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ints_printed = 0
    if x == 0:
        print()
        return ints_printed
    for item in my_list:
        try:
            print("{:d}".format(item), end='')
            ints_printed += 1
            if ints_printed == x:
                break
        except TypeError:
            break
        except ValueError:
            continue
    print()
    return ints_printed
