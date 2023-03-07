#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    new_string2 = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string = char + new_string
    for char in new_string:
        new_string2 = char + new_string2
    
    return (new_string2)

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
