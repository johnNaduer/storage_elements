#!/usr/bin/python3
def print_file_contents(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        file_contents = file.read()
        print(file_contents)

print_file_contents('2_example.txt')
