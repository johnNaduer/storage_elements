import doctest

def divide(a, b):
    """
    Divide dos números y devuelve el resultado.

    >>> divide(4, 2)
    2.0

    >>> divide(3, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return a / b

if __name__ == "__main__":
    doctest.testmod()
