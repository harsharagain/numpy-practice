# Higher Dimension Array

# Array can have any number of dimensions.
# Can define the number of dimensions by using the ``ndmin`` argument.

import numpy as np

arr = np.array([1, 2, 3], ndmin=5)

print('Number of Dimension:', arr.ndim) # Output: 5
print(arr) # Output: [[[[[1 2 3]]]]]
