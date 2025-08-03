num=int(input("number of students?"))
f=open("Students1.csv","a")
for i in range(num):
    name=input("what is your name?")
    age=int(input("how old are you?"))
    score=float(input("what is your score?"))
    f.write(f"{name},{age},{score}\n")
f.close()
