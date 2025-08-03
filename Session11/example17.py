f=open("Students2.csv","r")
for i in f.readlines():
    print(i.replace("\n","").replace(",","\t"))
f.close()
