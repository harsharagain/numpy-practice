# You can use -1 as a placeholder for an unknown dimension, and NumPy will calculate it for you.
# We can not pass -1 to more than one dimension.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, -1)

print(newarr) 
# Output:
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]