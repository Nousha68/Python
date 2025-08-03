for i in range(1,11):
    for j in range(1,11):
        if i==j:
            print("*",end="\t")
        else:
            print(i*j,end="\t")
    print()