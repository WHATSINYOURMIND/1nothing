# numpy program 2
# creating arrays/1d,2d,nd arrays in different ways possible

import numpy as np
import random

# initial way of creating an array and printing it
arr = np.array([1, 4, 8, 7, 5])
print(arr)

# create an array from list with data type float
a = np.array([[1, 4, 3], [6, 8, 9]], dtype='float')
print("ARRAY CREATED USING PASSED LIST\n", a)
# output with a decimal dot will be displayed

# Creating an array from tuple - set of collections which is ordered and unchangeable
b = np.array((1, 4, 4, 4, 3, 3, 3)) # parentheses insides parentheses is required to define a tuple
print("\n Array using tuples \n", b)
# duplicated values are allowed in tuples

# creating a matrix with all zereos - to use .zereos
c = np.zeros((2, 2)) # parentheses insides parentheses
print("\nTHE NULL MATRIX IS:\n", c)
# the data type is float

# Create a constant value of complex type
# complex data type prints complex numbers
d = np.full((2, 3), 4, dtype = 'complex')
print("\n Complex data type array is\n", d)
# 2,3 indicates the array dimensions and 4 here indiactes the value of x
# the y value will be printed in this case

# Creation of n dimensions array  using random values
e = np.random.random((1, 2))
print("ARRAY WITH RANDOM VALUES ARE \n", e)
# return type will be float

# creating a sequence of integers
# from 0 to 30 with a step of 7
f = np.arange(0, 30, 8)
print("\n The sequential array is\n", f)
# The arange function will begin with a specified limit and end to a specified limit and will print all the values, if not given any intervals.

# linspace - to print any n number of values between a, b including the first and last values
# where a is initial limit and b is the final limit
g = np.linspace(1, 8, 5)
print("\n sequential array with 10 values between 0 and 8 are\n", g)

# we can reshape the arrays as well - meaning?
# meaning - we can change a 2 by 3 matrix to 3 by 2 or 3 by 3
# lets see how
h = np.array([[1, 2, 3, 4],
              [2, 7, 6, 8],
              [1, 0, 8, 9]])
newarr = h.reshape(2, 2, 3)
# it wont accept every type of dimensions because of the changes in the number of elements

print("\n original array \n", h)
print("Reshaped array \n", newarr)

# FLATTEN ARRAY
arr1 = np.array([[2, 3, 4], [4, 2, 9], [0, 1, 5]])
flarr = arr1.flatten()

print("\n original \n", arr1)
print("Flattened array", flarr)
# flattened array brings all elements into one line



