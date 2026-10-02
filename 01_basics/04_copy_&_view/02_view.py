# Creating Views of Arrays in NumPy
# The view does not own the data and any changes made to the view will affect the original array and vice versa.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
newArr = arr.view()

arr[0] = 12

print(arr) # Output: [12  2  3  4  5]
print(newArr) # Output: [12  2  3  4  5]

newArr[1] = 22
print(arr) # Output: [12 22  3  4  5]
print(newArr) # Output: [12 22  3  4  5]