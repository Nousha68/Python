a=int(input("how many classmates do you have?"))
mylist=[]
for i in range(a):
    name=input("what is your name?")
    mylist.append(name)
print(mylist)
for i in mylist:
    print("hello" , i)