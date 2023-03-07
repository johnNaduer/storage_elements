#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_nueva_list = my_list.copy()
    my_nueva_list = list(set(my_nueva_list))
    x = 0
    suma = 0
    while x < len(my_nueva_list):
        suma = my_nueva_list[x] + suma
        x = x + 1
    return (suma)
