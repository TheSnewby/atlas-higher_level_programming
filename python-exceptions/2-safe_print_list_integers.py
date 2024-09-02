#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ints_printed = 0
    if x == 0:
        print()
        return ints_printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            ints_printed += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            raise IndexError("list index out of range")
    print()
    return ints_printed
