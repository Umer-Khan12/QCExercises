"""
Umer Khan
December 18th, 2020

Test drivers for each function in the project
"""

import ComplexNumbers as CN

print("Beginning test driver.\n")
numErrors = 0

"""
Tests for ComplexNumbers.py
"""
print("Beginning tests for ComplexNumbers.py.")
# Tests for getComplexNumber()
# Expected are the same as the elements in inputs as getComplexNumber() returns a tuple
inputs = [(0, 0), (-5, 2), (1.52, -5.2), (0, 1.5), (3, -4), (4, 4)]
for i in inputs:
    z = CN.getComplexNumber(i[0], i[1])
    if z != i:
        numErrors += 1
        print("Error in getComplexNumber(). Expected", CN.printComplexNumber(i), "but got", CN.printComplexNumber(z))

# Tests for add()
inputs = [((0, 0), (0, 0)), ((1, 0), (3, 4)), ((6, -3), (4, -2.5)), ((-2.2, 0.5), (4.3, -0.8))]
expected = [(0, 0), (4, 4), (10, -5.5), (-2.2 + 4.3, 0.5 - 0.8)]
expectedIndex = 0
for i in inputs:
    z1 = i[0]
    z2 = i[1]
    z = CN.add(z1, z2)
    if z != expected[expectedIndex]:
        numErrors += 1
        print("Error in add() for input,", CN.printComplexNumber(z1), "+", CN.printComplexNumber(z2),
              "Expected", CN.printComplexNumber(expected[expectedIndex]), "but got", CN.printComplexNumber(z))
    expectedIndex += 1

# Tests for multiply()
inputs = [((1, 2), (4, 1)), ((0.5, 1.5), (2, 5)), ((-4, -2.5), (2, 4.6))]
expected = [(2, 9), (-(13/2), 11/2), (-8+(5*4.6/2), -4 * 4.6 - 5)]
expectedIndex = 0
for i in inputs:
    z1 = i[0]
    z2 = i[1]
    z = CN.multiply(z1, z2)
    if z != expected[expectedIndex]:
        numErrors += 1
        print("Error in multiply() for input,", CN.printComplexNumber(z1) + CN.printComplexNumber(z2),
              "Expected", CN.printComplexNumber(expected[expectedIndex]), "but got", CN.printComplexNumber(z))
    expectedIndex += 1

print("\nTesting completed.", numErrors, "error(s) found.")
