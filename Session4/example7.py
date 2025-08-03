a=int(input("how many employers do you have?"))
namelist=[]
incomelist=[]
for i in range (a):
    name=input("what is your name?")
    income=int(input("how much is your income?"))
    namelist.append(name)
    incomelist.append(income)
print(namelist)
print(incomelist)
for i in range(a):
    print(namelist[i], incomelist[i])