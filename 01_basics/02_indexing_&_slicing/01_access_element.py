import numpy as np

#1d_arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr[0]) #Output: 1

#2d_arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('2nd column, 1st row:', arr[0][1]) #Output: 2

#3d-arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('third element of the second array of the first array:', arr[0][1][2]) #Output: 6

#Negative-indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #Output: 10