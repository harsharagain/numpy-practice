# Copying Arrays in NumPy
# The copy owns the data and any changes made to the copy will not affect original array
# Any changes made to the original array will not affect the copy.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
newarr = arr.copy()

newarr[0] = 9

print(arr) # Output: [1 2 3 4 5]
print(newarr) # Output: [9 2 3 4 5]

arr[0] = 24
print(arr) # Output: [24  2  3  4  5]