#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_replace = []
    x = 0
    while x < len(my_list):
        if my_list[x] == search:
           list_replace.append(replace)
        else:
            list_replace.append(my_list[x])
        x = x + 1
    return (list_replace)
