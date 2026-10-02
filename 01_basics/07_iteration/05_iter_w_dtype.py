# Iterating Array with Different Data Types

# We can use `op_dtypes` argument and pass it the expected datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the element is in array) 
# So it needs some other space to perform this action, that extra space is called buffer
# In order to enable it in nditer() we pass flags=['buffered']

import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Output:
# np.bytes_(b'1')
# np.bytes_(b'2')
# np.bytes_(b'3')