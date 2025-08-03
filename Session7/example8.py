r=int(input("the number of rows? "))
c=int(input("the number of columns? "))
name=input("tell me your name?")
for i in range(r):
    for j in range(c):
        print(name, end="\t")
    print()
