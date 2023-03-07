#!/usr/bin/python3
def only_diff_elements(set_1, set_2):    
    nuevo_set_1 = list(set_1)
    nuevo_set_2 = list(set_2)
    x = 0
    common_element = []
    while x < len(nuevo_set_1):
        y = 0
        while y < len(nuevo_set_2):
            if nuevo_set_1[x] != nuevo_set_2[y]:            
                common_element.append(nuevo_set_1[x])
                common_element.append(nuevo_set_2[y])
            y = y + 1
        x = x + 1
    return (common_element)
