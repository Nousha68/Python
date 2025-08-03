number=int(input("number of costumers?"))
namelist=list()
billlist=list()
saleslist=list()
for i in range(number):
    name=input("costomer's name?")
    bill=int(input("number of bills?"))
    sale=int(input("sales amount?"))
    namelist.append(name)
    billlist.append(bill)
    saleslist.append(sale)
for i in range(number):
    print(namelist[i],billlist[i],saleslist[i])
n=int(input("higher saleslist?"))
for i in range(number):
    if n<=saleslist[i]:
        print(namelist[i], billlist[i], saleslist[i])