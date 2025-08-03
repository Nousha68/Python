a=int(input("number 1"))
b=int(input("number 2"))
if a>b:
    print(" a is larger ")
    if (a-b)%2==0:
        print("a-b=even")
    else:
        print("a-b=odd")
elif a==b:
    print("a equals b ")
    print("a-b=even")
else:
    print(" b is larger")
    if (b-a)%2==0:
        print("b-a=even")
    else:
        print("b-a=odd")
