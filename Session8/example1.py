import numpy as np
a=[1,2,3,4]

print(a[1:3])
b=np.array(a)
print(b[1:3])
a=[
    [1,2,3,6],
    [4,5,6,8],
    [9,8,3,2]
]
print(a[2])
print(a[2][0])
X=np.array(a)
print(X[0::2])#start:end:step
print(X[:,1::2])
print(X[1::2,::2])
