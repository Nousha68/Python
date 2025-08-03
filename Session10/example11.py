f=open("employee.csv","r")
a=f.readlines()
for i in range(len(a)):
    a[i]=a[i].replace("\n","")
print(a)
for i in a:
    print(i.replace("\n",""))

f.close()