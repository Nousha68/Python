from coloroma import Back
for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
             print(Back.BLACK, end="\t")
        else:
            print(Back.WHITE,end="\t")
    print(Back.RESET)
