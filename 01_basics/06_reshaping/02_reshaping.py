# Reshaping from 1-D to 3-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newArr = arr.reshape(2, 3, 2)

print(newArr)
# Output:
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]