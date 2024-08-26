#!/usr/bin/python3
for i in range(0, 100):
    print((", " if i > 0 else "") + "{:0>{}}".format(i, 2), end="")
print()
