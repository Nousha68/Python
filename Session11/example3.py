number=int(input("number of employee?"))
f=open("employee.txt","w")
for i in range(number):
    name=input("what is your name?")
    f.write(name+"\n")

f.close()
