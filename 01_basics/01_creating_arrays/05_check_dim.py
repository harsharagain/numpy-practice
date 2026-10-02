import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a.ndim) # Output: 0
print(b.ndim) # Output: 1
print(c.ndim) # Output: 2
print(d.ndim) # Output: 3

