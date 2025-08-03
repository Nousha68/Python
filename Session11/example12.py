num=int(input("number of teachers?"))
f=open("Teachers.csv","a")
# f.write("name,age, grade, Salary,gradestatuse\n")
for i in range(num):
    name=input("what is your name?")
    age=int(input("how old are you?"))
    grade=input("what is your grade?")
    salary=int(input("how much is your salary?"))
    gradestatuse=""
    if grade=="A":
        if 1000<=salary<2000:
            gradestatuse="correct"
        else:
            gradestatuse="false"
    elif grade=="B":
        if 2000<=salary<3000:
            gradestatuse="correct"
        else:
            gradestatuse = "false"
    elif grade=="C":
        if 3000<=salary<4000:
            gradestatuse = "correct"
        else:
            gradestatuse = "false"
    else:
        gradestatuse="grade not valid"
    f.write(f"{name},{age},{grade},{salary},{gradestatuse}\n")
f.close()
