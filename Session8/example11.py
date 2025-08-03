a=int(input("tell a number"))
i=0
while i<=a:
    if i%2==0:
        print(i,"even",end="\t")
    if i%3==0:
        print(i,"divided 3", end="\t")
    if i%5==0:
        print(i, "divide 5",end="\t")
    if i%11==0:
        print(i,"divide 11",end="\t")
    print()
    i=i+1

