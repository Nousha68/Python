a=int(input("how many friends do you have?"))
namelist=[]
i=0
while i<a:
    name=input("what is her/his name?")
    namelist.append(name)
    i=i+1
print(namelist)
b=0
while b<len(namelist):
    print("hi", namelist[b])
    b=b+1