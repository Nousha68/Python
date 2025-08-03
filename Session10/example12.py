num=int(input("number of students?"))
file=open("student.csv","w")
file.write("name,age,score\n")
for i in range(num):
    name=input("what is your name?")
    age=int(input("how old are you?"))
    score=float(input("what is your score"))
    file.write(f"{name},{age},{score}\n")
file.close()