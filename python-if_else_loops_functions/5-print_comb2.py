#!/usr/bin/python3
for i in range(0,100):
	if i > 0:
		print(", ", end = "")
	print(str(i).zfill(2), end = "")
