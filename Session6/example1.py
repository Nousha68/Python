from colorama import Fore,Back
for i in range(1,11):
    for j in range(1,11):
        if j%2==0:
            print(Back.RESET+Fore.BLUE+ str(i*j), end="\t")
        else:
            print(Back.RED+str(i*j),end="\t")
    print()
