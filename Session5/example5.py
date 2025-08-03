for i in range(1,11):
    for j in range(1,11):
        if i%2==0 or j%2==0:
            print("*",end="\t")
        else:
            print(i*j,end="\t")
    print()