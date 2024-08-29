#!/usr/bin/python3

import hidden_4

if __name__ == "__main__"":
    names = dir(hidden4)
    names = sorted(names)
    for i in range(len(names)):
        if names[i][0] == '_' and names[i][1] == '_':
            names.remove(i)
        else:
            print('{}'.format(names[i]))

