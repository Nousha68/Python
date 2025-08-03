for i in range(1,11):
    for j in range(1,11):
        if (i==j and j>5): #or i==1 or j==1 or i==10 or j==10 or (i+j==11 and i<6 ):
            print("*",end="\t")

        else:
            print(i*j, end="\t")
    print()