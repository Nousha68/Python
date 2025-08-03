a=int(input(" number 1 "))
b=int(input("number 2"))
if b>=a:
    if (a-b)%2==0:
        for i in range(a,b):
            print(i**2)
    else:
        for i in range(a,b):
            print(i**3)
else:
    if (a-b)%2==0:
        for i in range(b,a):
            print(i**2)
    else:
        for i in range(b,a):
            print(i**3)