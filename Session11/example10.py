num=int(input("number of students?"))
f=open("Students3.csv","w")
f.write("name,age,score,scorestatuse,agestatuse\n")
for i in range(num):
    name=input("what is your name?")
    age=int(input("how old are you?"))
    score=float(input("what is your score?"))
    scorestatuse=""
    if score <=12:
        scorestatuse="fail"
    else:
        scorestatuse="pass"
    agestatuse=""
    if 0<=age<12:
        agestatuse="child"
    elif 12<=age<18:
        agestatuse="teenager"
    elif 18<=age<23:
        agestatuse="young"
    elif 23<=age:
        agestatuse="older than class renge age"
    else:
        agestatuse="invalid"

    f.write(f"{name},{age},{score},{scorestatuse},{agestatuse}\n")
f.close()