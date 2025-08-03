i=1
while i<11:
    j=1
    while j<11:
        if i==j or i==1 or i==10 or j==1 or j==10 or i+j==11:
            print("*",end="\t")
        else:
            print(end="\t")
        j=j+1
    i=i+1
    print()