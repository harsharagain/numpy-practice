# Stacking along height (depth)

# dstack() function is used to stack arrays in sequence depth wise (along third axis).
# stacks along height, which is the same as depth.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
# Output:
# [[[1 4]
#   [2 5]
#   [3 6]]]