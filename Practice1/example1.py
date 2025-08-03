a=int(input ("number 1 "))
b=int(input ("number 2 "))
c=int(input ("number 3 "))
if a>b and a>c:
    print( str(a) + " is larger than " +str(b)+ " and larger than "+ str(c))
elif b>a and b>c:
    print(str(b) + " is larger than " + str(a)+ " and larger than " + str(c))
elif c>a and c>b:
    print(str(c) + " is larger than" + str(a) +" and larger than " + str(b))
else:
    print("all or some numbers are equal")