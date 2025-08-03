number=int(input("how many students?"))
namelist=list()
weightlist=list()
hightlist=list()
for i in range(number):
    name=input("waht is your name?")
    weight=float(input("your weight?"))
    height=int(input("your height?"))
    namelist.append(name)
    weightlist.append(weight)
    hightlist.append(height)
for i in range(len(namelist)):
    print(namelist[i], weightlist[i],hightlist[i])