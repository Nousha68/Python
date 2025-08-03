for i in range(1,11):
    for j in range(1,11):
        if i==j or i+j==11:
            print("*",end="\t")
        else:
            print("",end="\t")
    print()
