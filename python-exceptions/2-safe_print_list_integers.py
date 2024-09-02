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

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))