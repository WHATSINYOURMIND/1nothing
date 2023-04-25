# numerical python program
# basic array characteristics
# This program consist of the basic structrue of an array
# that is created in a python program and a few of its functions too.
import numpy as np

# creating array object with 2 rows and columns - it becomes a matrix
arr = np.array([[1, 2, 3, 4, 5],
               [2, 7, 6, 4, 3]])
print(arr)

# printing array dimensions
print("NO OF DIMENSIONS: ", arr.ndim)

# printing type of arr object
print("ARRAY IS OF TYPE: ", type(arr))

# printing shape of array - (x,y)
print("SHAPE OF ARRAY: ", arr.shape)

# printing total number of elements in the array
print("NUMBER/SIZE OF ARRAY IS: ", arr.size)

# printing type of elements in array
print("ARRAY STORES ELEMENTS OF TYPE: ", arr.dtype)

# .size , .shape , .type , .dtype - int32 or int64 in the above example
# .type(array variable)

# numpy - library and whenever we import it we get an object of it - np
# using np we create different types of array in numerical python

