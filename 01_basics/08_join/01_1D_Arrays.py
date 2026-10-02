# concatenate() function allows us to join two or more arrays along an existing axis.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr) # Output: [1 2 3 4 5 6]