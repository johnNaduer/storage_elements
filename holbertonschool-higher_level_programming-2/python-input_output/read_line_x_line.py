#!/usr/bin/python3
count = 0

with open('new_file.txt') as _file:

    while True:
        line = _file.readline()
        if not line:
            break
        print(line)
        count += 1
