for i in range(1,11):
    for j in range(1,11):
        if i==1 or i==10:
            print("=", end="\t")
        elif j==1 or j==10:
            print("*", end="\t")
        elif i==j:
            print("\\", end="\t")
        else:
            print(i*j, end="\t")
    print()