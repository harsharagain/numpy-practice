# Changing data type from one data type to another data type is called Type Casting. 
# We can use astype() function to cast data types.

import numpy as np

arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(arr.dtype) # Output: float64

newarr = arr.astype('i')
print(newarr) # Output: [1 2 3 4 5]
print(newarr.dtype) # Output: int32

