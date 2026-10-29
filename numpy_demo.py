# import numpy as np 

# arr= np.array([10,20,30,40,50])
# print("Array:",arr)
# print("sum:",np.sum(arr))
# print("Max:",np.max(arr))


import numpy as np

# Create a 2D array
arr = np.array([[5, 2, 4],
                [1, 2, 4]])

print("2D Array:")
print(arr)

print("Element at row 1, column 2:", arr[0][1])
print("Number of rows and columns:", arr.shape)


import numpy as np

# Create a 3D array
arr = np.array([
    [[2, 4, 1],
     [4, 2, 5]],

    [[7, 8, 9],
     [10, 11, 12]]
])

print("3D Array:")
print(arr)

print("Shape of array:", arr.shape)
print("First element:", arr[0][0][0])


# 1D Array Operations in NumPy

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array:", a)

print("Addition:", a + 5)
print("Subtraction:", a - 5)
print("Multiplication:", a * 2)
print("Division:", a / 10)

print("Sum:", np.sum(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Mean:", np.mean(a))

# 2D Matrix Operations

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:") 
print(A)

print("Matrix B:")
print(B)

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Element-wise Multiplication:")
print(A * B)

print("Matrix Multiplication:")
print(A @ B)

print("Transpose of A:")
print(A.T)