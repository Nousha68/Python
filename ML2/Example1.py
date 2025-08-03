import numpy as np
a=np.array([1,2,5,87, 45, 23, 54, 34])
print(type(a))
print(a)
print(a[1])
print(a.shape)
print(a.size)
print(a.ndim)
b=np.array([
    [43, 65, 87, 91],
    [10, 20, 30, 40],
    [22, 33, 44, 55]
])
print(type(b))
print(b)
print(b[1])
print(b[1, 3])
print(b[1:])
print(b[1:,2:])
print(b[1:,2])
print(b[:,3:])
print(b[:,-1:])
print(b[-1:,-1])
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)