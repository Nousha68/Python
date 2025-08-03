from colorama import Fore
for i in range(1,11):
    for j in range(1,11):
        if j%2==0 and i%2==0:
             print(Fore.BLUE+str(i*j), end="\t")
        else:
            print(Fore.RED+str(i*j),end="\t")
    print()
