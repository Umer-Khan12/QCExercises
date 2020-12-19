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


def add(z1, z2):
    """
    Given two complex numbers z1, z2, returns the complex
    number z1 + z2.
    """
    return getComplexNumber(z1[0] + z2[0], z1[1] + z1[1])
