#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    x = 0
    while x < len(my_list):
        print("{}".format(my_list[x]))
        x = x + 1
