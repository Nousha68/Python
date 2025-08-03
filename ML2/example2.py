import numpy as np
a=np.array([
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ],
    [
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ]
])
print(type(a))
print(a.shape)
print(a.ndim)
print(a.size)
print(a)
print("?"*25)
print(a[1])
print(a[:,0])
print("?"*25)
print(a[:,:, -1])
print(a[:, ::2, ])
print("?"*25)
print(a[:,:, 1::2])
print(a[:,1::2,::2 ])
print("?"*25)
print(a[-1,-1,-1])
print(a[-1,::2,1::2])
print(a[:,1:,2:])
print(a[:,2,3])
print(a[:,-1,-1])
print("?"*25)
print(a[:,:, -1])
print(a[:, ::2, ])