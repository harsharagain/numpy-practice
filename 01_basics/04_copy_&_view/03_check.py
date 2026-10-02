# Check if Array Owns it's Data
# The `base` attribute returns the base object if the array is a view of another array.
# If the array owns the data, the base is None.
# The view returns the original array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
newArr = arr.copy()
newArr2 = arr.view()

print(arr.base) # Output: None
print(newArr.base) # Output: None
print(newArr2.base) # Output: [1 2 3 4 5]