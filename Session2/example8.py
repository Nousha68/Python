a=float(input("give me a number"))
b=float(input("give me the second number"))
c=float(input("give me another number"))
if a>=b:
    if a>=c:
        print( str(a) + " is larger than " +str(b)+ " and "+ str(c))
    else:
        print( str(c) + " is larger than " + str(a)+ " and " +  str(b))
else:
    if b>=c:
        print(str(b) + " is larger than " + str(a) +   " and " + str(c))
    else:
        print( str(c)+ " is larger than " + str(a) + " and " + str(b))
