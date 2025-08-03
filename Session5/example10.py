for i in range(1,11):
    for j in range(1,11):
        if j==1 or j==10 or i==j:
            print("*",end="\t")
        else:
            print(end="\t")
    print()