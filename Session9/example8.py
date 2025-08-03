number=int(input("how many students?"))
namelist=list()
weightlist=list()
hightlist=list()
i=0
while i<number:
    name=input("waht is your name?")
    weight=float(input("your weight?"))
    height=int(input("your height?"))
    namelist.append(name)
    weightlist.append(weight)
    hightlist.append(height)
    i=i+1
i=0
while i< range(len(namelist)):
    print(namelist[i], weightlist[i],hightlist[i])
    i=i+1