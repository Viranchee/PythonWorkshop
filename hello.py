#!/usr/bin/env python3
print("Hello World")
print("Hello World")

someVariable = "Hello World"

print(someVariable)

print(type(someVariable))
print(type(5))

someVariable = 5
print(type(someVariable))

otherVariable = someVariable
otherVariable += 5
print(otherVariable)
print(someVariable)

array1 = [0,0,0,0]
array2 = array1
array2[3] = 5
print(array1)
print(__name__)
print(__file__)

import inspect
print(inspect.currentframe().f_lineno)

def debugThis():
    print(inspect.stack()[1][1],":",inspect.stack()[1][2],":", inspect.stack()[1][3])
    print("This function is " + inspect.stack()[0][3])

print(inspect.stack()[0][4])
line33caller = inspect.stack()[0][2]
print(line33caller)

debugThis()
print(__package__)
print(__debug__)