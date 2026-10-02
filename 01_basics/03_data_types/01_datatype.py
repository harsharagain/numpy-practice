# Checking the data type of an array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype) # Output: int32

arr = np.array(['banana', 'grapes', 'apple'])
print(arr.dtype) # Output: <U6

# Ref: https://www.geeksforgeeks.org/numpy/numpy-data-types/