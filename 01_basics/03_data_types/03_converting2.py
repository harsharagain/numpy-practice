import numpy as np

arr = np.array([1.1, 2.1, 3.1, 4.1, 0])
newarr = arr.astype(bool)

print(newarr) # Output: [ True  True  True  True  False]
print(newarr.dtype) # Output: bool