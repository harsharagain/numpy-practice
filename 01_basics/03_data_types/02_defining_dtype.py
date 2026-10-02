# Creating arrays with a defined data type
# dtype is a special object that specifies the type of data that the array will hold. 
# It can be specified when creating an array using the dtype parameter.

import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr.dtype) # Output: |S1

# For i, u, f, S and U we can define size as well.

arr = np.array([1, 2, 3, 4, 5], dtype='i4')
print(arr.dtype) # Output: int32