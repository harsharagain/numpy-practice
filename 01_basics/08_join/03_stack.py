# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1) # Stacking along axis 1 means that the arrays will be stacked as columns.
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

arr = np.stack((arr1, arr2))
print(arr)
# Output:
# [[1 2 3]
#  [4 5 6]]

