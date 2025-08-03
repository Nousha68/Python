for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print()
i=1
while i<11:
    j=1
    while j<11:
        print(i*j, end="\t")
        j=j+1
    i=i+1
    print()