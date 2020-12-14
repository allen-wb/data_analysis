import numpy as np

a = np.arange(15).reshape(3, 5)
b = np.array([4, 5, 6], ndmin=2, dtype=complex)
print(a)
print("-----")
print(b)

ar = np.array([1, 2, 3, 4, 5, 6, 7])
print(ar)
print(ar.shape)
print(ar.size)
print(ar.ndim)

