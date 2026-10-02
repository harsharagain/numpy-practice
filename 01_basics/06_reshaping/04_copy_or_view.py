# Copy or View?
# When you use the reshape() method, it returns a view of the original array, not a copy.
# This means that the original array is affected when you change the shape of the view.
# It is a view of the original array, and any changes made to the view will also affect the original array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # Output: [1 2 3 4 5 6 7 8]

newArr = arr.reshape(2, 4)
print(newArr.base) # Output: [1 2 3 4 5 6 7 8]



