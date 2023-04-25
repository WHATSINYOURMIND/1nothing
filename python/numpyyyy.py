#multipication(dot)
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)
 #multiplication (outer)

import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result = np.outer(p, q)
print("Outer product of the said two vectors:")
#einstein summation
Note: In mathematics, especially in applications of linear algebra to physics, the Einstein notation or
Einstein summation convention is a notational convention that implies summation over a set of
indexed terms in a formula, thus achieving notational brevity.
import numpy as np
a = np.array([1,2,3])
b = np.array([0,1,0])
print("Original 1-d arrays:")
print(a)
print(b)
result = np.einsum("n,n", a, b)
print("Einstein’s summation convention of the said arrays:")
print(result)
x = np.arange(9).reshape(3, 3) y = np.arange(3, 12).reshape(3, 3)
print("Original Higher dimension:")
print(x)
print(y)
result = np.einsum("mk,kn", x, y)
print("Einstein’s summation convention of the said arrays:")
print(result)

#determinant
import numpy as np
a = np.array([[1,2],[3,4]])
print("Original array:")
print(a)
result = np.linalg.det(a)
print("Determinant of the said array:")
print(result)
#sum of digonal element

import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result = np.trace(m)
print("Condition number of the said matrix:")
print(result)
#to compute the factor of a given array by Singular Value
Decomposition.
import numpy as np
a = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.f
print("Original array:")
print(a)
U, s, V = np.linalg.svd(a, full_matrices=False)
print("Factor of a given array by Singular Value Decomposition:")
print("U=\n", U, "\ns=\n", s, "\nV=\n", V)
#calculate the Frobenius norm and the condition number of a given array
import numpy as np
a = np.arange(1, 10).reshape((3, 3))
print("Original array:")
print(a)
print("Frobenius norm and the condition number:")
print(np.linalg.norm(a, 'fro'))
print(np.linalg.cond(a, 'fro'))
 #Reverse
 import numpy as np
import numpy as np
x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:") x = x[::-1]
print(x)
# create an 8x8 matrix and fill it with a checkerboard pattern
import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:") x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)
#convert a list and tuple into array
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(my_tuple))

#coversion Centigrade degrees into Fahrenheit degrees
import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91, 32] F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in Centigrade degrees:")
print(np.round((5*F/9 - 5*32/9),2))
#Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in array1 that are not in array2
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))
# create a 5x5 matrix with row values ranging from 0 to 4
import numpy as np
x = np.zeros((5,5))
print("Original array:")
print(x)
print("Row values ranging from 0 to 4.") x += np.arange(5)
print(x)
             
