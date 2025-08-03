num=int(input("number of students?"))
f=open("Students.csv","w")
for i in range(num):
    name=input("what is your name?")
    f.write(name+"\n")

f.close()