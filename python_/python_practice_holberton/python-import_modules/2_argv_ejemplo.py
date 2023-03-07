#!/usr/bin/python3
import sys

# check that the correct number of arguments were passed
if len(sys.argv) != 3:
    print("Usage: python script.py arg1 arg2")
    sys.exit()

# assign the input arguments to variables
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# do something with the input arguments
result = int(arg1) + int(arg2)

# print the result
print("The result is:", result)
