for i in range(1,11):
    for j in range(1,11):
        if (i==j and j>5) or (i+j==11 and j>5) or j==5 or j==6:
            print("*",end="\t")
        else:
            print(end="\t")
    print()