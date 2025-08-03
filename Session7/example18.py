from colorama import Fore,Back
r=int(input("number of row"))
c=int(input("number of column"))
for i in range (r):
    for j in range(c):
        if j==0:
            print(Back.RED, end="\t")
        elif j==1:
            print(Back.WHITE,end="\t")
        elif j==2:
            print(Back.GREEN,end="\t")
        elif j==3:
            print(Back.BLUE, end="\t")
        elif j==4:
            print(Back.CYAN, end="\t")
        else:
            print(Back.BLACK, end="\t")

    print(Back.RESET)