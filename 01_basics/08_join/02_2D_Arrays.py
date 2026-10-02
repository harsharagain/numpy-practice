# Joining 2-D Arrays along rows (axis = 1)

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr) 
# Output:
# [[1 2 5 6]
# [3 4 7 8]]

# Without using (axis=1)
arr = np.concatenate((arr1, arr2))
print(arr)
# Output:
# [[1 2]
# [3 4]
# [5 6]
# [7 8]]