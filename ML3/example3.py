import numpy as np
a=int(input("1.vector\n2.matrix\n3.cube"))
if a==1:
    b=int(input("the number of vector member"))
    v=np.random.randint(1,7,b)
    print(v)
elif a==2:
    r=int(input("the number of matrix row"))
    c=int(input("the number of matrix column"))
    l=int(input("the lowest number"))
    h=int(input("the highest number"))
    m=np.random.randint(l,h,(r,c))
    print(m)
elif a==3:
    r=int(input("number of row"))
    c=int(input("number of column"))
    m=int(input("number of matrix"))
    cube=np.zeros((m,r,c))
    print(cube)
else:
    print("the number is not valid")