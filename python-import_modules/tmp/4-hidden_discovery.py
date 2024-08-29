#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    names = sorted(names)
    for name in names:
        if name[0] == '_' and name[1] == '_':
            names.remove(name)
        else:
            print('{}'.format(name))

