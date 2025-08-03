num=int(input("number of students?"))
f=open("Students2.csv","w")
f.write("name,age,score,scorestatuse\n")
for i in range(num):
    name=input("what is your name?")
    age=int(input("how old are you?"))
    score=float(input("what is your score?"))
    scorestatuse=""
    if score <=12:
        scorestatuse="fail"
    else:
        scorestatuse="pass"

    f.write(f"{name},{age},{score},{scorestatuse}\n")
f.close()
