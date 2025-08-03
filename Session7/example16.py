from colorama import Fore
for i in range(1,11):
    for j in range(1,11):
        if i%2==0:
            if j%2==0:
                print(Fore.GREEN+str(i*j),end="\t")
            else:
                print(Fore.BLUE+str(i*j),end="\t")
        else:
            if i%2==1:
                print(Fore.WHITE+str(i*j),end="\t")
            else:
                print(Fore.RED+str(i*j), end="\t")
    print()