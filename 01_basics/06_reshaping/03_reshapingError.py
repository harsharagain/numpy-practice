# Reshaping Error

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newArr = arr.reshape(3, 4, 2)
# This will raise a ValueError 
# because the total number of elements (12) does not match the product of the new shape dimensions (3 * 4 * 2 = 24)
