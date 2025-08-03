a=int(input("tell a number"))
for i in range(1,a):
    if i%2==0:
        print(i,i**3,sep="=")
    else:
        print(i,i**2,sep="=")