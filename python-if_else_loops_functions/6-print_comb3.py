#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if (i * 10 + j != 1):
            print(", ", end="")
        print(str(i * 10 + j).zfill(2), end="")
print("\n")
