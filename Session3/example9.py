a=int(input("number 1 "))
b=int(input("number 2 "))
for i in range(a,b):
    if i%2==0:
        print(i**2)
    else:
        print(i**3)