# this program gives operations to be performed on array
# also the sorting process 
import numpy as np

a1 = np.array([2, 8, 9, 12, 6.8, -1])

# part 1
# add any number to every element
print("Adding any number to every element :", a1+6)

# subract any number from every element
print("subracting a number from any element :", a1-6)

# multiplication ,division , squaring are possible on an array
# transpose of an array
a2 = np.array([[1, 2, 3],
               [9, 6, 8],
               [8, 6, 0]])

print("\nOriginal Array:\n", a2)
print("\nTranspose Array:\n", a2.T)

# Part 2
# we will use a2 array as an example for unary operations

# to print Largest element of the matrix
print("Largest element in the entire array is\n", a2.max())

# the following max has axis as 1 , which means maximum element of every row will be chosen and printed in the lists
print("row-wise max elements are \n", a2.max(axis=1))
# axis =1 for row and axis=0 for columns
print("column-wise min elements are\n", a2.min(axis=0))

# sum of array elements - array_name.sum()
print("CUMULATIVE SUM ALONG EACH ROW\n", a2.cumsum(axis=1))

# binary operations - where two diff arrays can be added/subracted/multiplied

a3 = np.array([[1, 2],
              [4, 8]])
b1 = np.array([[6, 7],
              [10, 20]])

# adding array elements
print("array sum\n", a3+b1)
# multiplying array elements
print("Array multiplication(elementwise)\n", a3*b1)
# Multiplication of matrix
print("Matrix Multiplication\n",a3.dot(b1))

# universal functions - sin , cos, tan , sqrt , exp etc
a4 = np.array([0, np.pi/2, np.pi])
print("sin values of it\n", np.sin(a4))

a5 = np.array([0, 10, 2, 14, 9, 12])
print("Expo of all array elements\n", np.exp(a5))

# Sorting
# with respect to a5 and a2
print("array elements in sorted order\n ", np.sort(a5)) # single dimensional array

# row-wise sorted array and column-wise sorted array
print("row-wise sorted array \n", np.sort(a2, axis=1, kind='mergesort'))

# Example of sorting of structured array
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# values to be put in array
values = [('Hrithik', 2002, 6.8), ('Laksh', 2025, 9.7),
          ('Akshay', 2000, 7.2), ('Aakash', 2023, 7.0)]

# Creating array
arr = np.array(values, dtype=dtypes)
print("\nArray sorted by names:\n",
      np.sort(arr, order='name'))

print("Array sorted by graduation year and then cgpa:\n",
      np.sort(arr, order=['grad_year', 'cgpa']))

# np as the object 
# np.array(array variable)
# inside the bracket we can specify the type of sorting to be done and also the axis if there is a matrix
# we can also sort array wrt names , graduation year - structured array
