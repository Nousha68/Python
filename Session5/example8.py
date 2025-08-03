for i in range(1,11):
    for j in range(1,11):
        if i==j or i+j==11 or j==1 or j==10 or j==5 or j==6:
            print("*",end="\t")
        else:
            print(end="\t")
    print()