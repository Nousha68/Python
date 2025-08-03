f=open("Teachers.csv","r")
a=f.readlines()
for i in a:
    print(i)
f.close()