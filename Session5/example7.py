for i in range(1,11):
    for j in range(1,11):
        if i==j:
            print(i*j,end="\t")
        else:
            print("@", end="\t")
    print()