f=open("Teachers.csv","r")
a=f.readlines()
for i in a:
    print(i.replace("\n","").replace(",","\t"))
f.close()