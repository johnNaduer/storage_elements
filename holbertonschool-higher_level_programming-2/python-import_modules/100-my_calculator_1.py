#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Uso: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Operador desconocido. Operadores disponibles: +, -, * y /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))

"""
if __name__ == "__main__":
    from sys import argv    
    from calculator_2 import add, sub, mul, div
    
    if argv[2] == "+":
        print(add(int(argv[1]),int(argv[3])))
    elif argv[2] == "-":
            print(sub(int(argv[1]),int(argv[3])))
    elif argv[2] == "*":
            print(mul(int(argv[1]),int(argv[3])))
    elif argv[2] == "/":
            print(div(int(argv[1]),int(argv[3])))
"""
