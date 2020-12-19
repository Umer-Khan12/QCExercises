"""
Umer Khan
December 18th, 2020
Functions for various computations involving complex numbers
"""


def getComplexNumber(a, b):
    """
    Given real numbers a and b, returns a tuple (a, b)
    that represents the complex number a+bi.
    """
    return a, b


def printComplexNumber(z):
    """
    Given a tuple representing a complex number,
    return a string representation of that complex number.
    """
    return "(" + str(z[0]) + " + " + str(z[1]) + "i" + ")"


def add(z1, z2):
    """
    Given two complex numbers z1, z2, returns the complex
    number z1 + z2.
    """
    return getComplexNumber(z1[0] + z2[0], z1[1] + z2[1])


def multiply(z1, z2):
    """
    Given two complex numbers z1, z2, returns the complex
    number (z1)(z2) using the following formula:
    (a + bi)(c + di) = (ac - bd) + (ad + bc)i
    """
    a = (z1[0] * z2[0]) - (z1[1] * z2[1])
    b = (z1[0] * z2[1]) + (z2[0] * z1[1])
    return getComplexNumber(a, b)
