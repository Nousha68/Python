import numpy as np
a=np.random.rand(4,3,5)
print(a)

c=["red","green","black"]
b=np.random.choice(c)
print(b)
b=np.random.choice(c,size=2,replace=False)
print(b)
b=np.random.choice(c,size=2,replace=True)
print(b)
b=np.random.choice(c,size=4,replace=True)
print(b)
