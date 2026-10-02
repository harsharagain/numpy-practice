import numpy as np

# Slicing 1-D Arrays
print("Slicing 1-D Arrays")
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:3]) # Output: [2 3]
print(arr[:3]) # Output: [1 2 3]
print(arr[3:]) # Output: [4 5]
print(arr[::2]) # Output: [1 3 5]
print(arr[-4:-1]) # Output: [2 3 4]

# Slicing 2-D Arrays
print("Slicing 2-D Arrays")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# From the second element, slice elements from index 1 to index 4 (not included)
print(arr[1, 1:4]) # Output: [7 8 9]

# From both elements, slice index 2
print(arr[0:2, 2]) # Output: [3 8]

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array 
print(arr[0:2, 1:4]) # Output: [[2 3 4] [7 8 9]]

