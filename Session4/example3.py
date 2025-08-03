a=int(input("give me the list of numbers"))
mylist=[]
mylist1=list()
for i in range(a):
    s=float(input("tell a number"+ str(i+1)))
    mylist.append(s)
print(mylist)
for i in mylist:
    if i>=12:
        print(i,"pass")
    else:
        print(i, "fail")