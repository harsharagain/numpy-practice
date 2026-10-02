# Reshaping means changing the shape of an array
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Reshape from 1-D to 2-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newArr = arr.reshape(4, 3)

print(newArr) 
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

