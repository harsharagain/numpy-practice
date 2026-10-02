# Shape of an Array is the number of elements in each dimension.
# Shape is a tuple of integers that indicate the size of the array in each dimension.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # Output: (2, 4)
# The array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape) # Output: (1, 1, 1, 1, 4)
# The array has 5 dimensions, where the first four dimensions have 1 element each, and the last dimension has 4 elements.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # Output: (2, 3)
# The array has 2 dimensions, where the first dimension has 2 elements and the second has 3.

