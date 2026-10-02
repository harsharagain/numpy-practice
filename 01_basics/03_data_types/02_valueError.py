# If a type is given in which elements cannot be casted, a ValueError is raised by NumPy
# ValueError: Raised when type of passed argument is incorrect

import numpy as np

arr = np.array(['a', 'b','5', '2'], dtype='i')
print(arr.dtype) # Output: ValueError: invalid literal for int() with base 10: 'a'

