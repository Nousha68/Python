a=int(input("tell a number"))
i=0
while i<=a:
    if i%2==0:
        print(i,"multiply 2",end="\t")
    if i%3==0:
        print(i,"multiply 3",end="\t")
    if i%5==0:
        print(i, "multiply 5",end="\t")
    i=i+1
    print()