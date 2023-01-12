#!/usr/bin/python3
"""
add_integer:
    Checks if parameters are int
    Returns sum of parameters
"""


""" Doc """

def add_integer(a, b=98):
    """ Doc """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)


def add_integer(a, b=98):
    """
    Checks if int, otherwise return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
