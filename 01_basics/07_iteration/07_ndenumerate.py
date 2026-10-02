# Enumerated Iteration Using ndenumerate()
# Enumerated iteration allows us to iterate through an array and have an automatic counter. 
# The counter can be used to keep track of the index of the current value.

import numpy as np

arr = np.array([5, 3, 8, 4])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
# Output:
# (0,) 5
# (1,) 3
# (2,) 8
# (3,) 4

arr = np.array([[1, 2, 3], [4, 5, 6]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
# Output:
# (0, 0) 1
# (0, 1) 2
# (0, 2) 3
# (1, 0) 4
# (1, 1) 5
# (1, 2) 6