num=int(input("number of employee"))
f=open("emp.csv","w")
f.write("name,age,salary,agestatus,salarystatuse\n")
for i in range(num):
    name=input("what is your name?")
    age=int(input("how old are you?"))
    salary=int(input("how much is your income?"))
    agestatuse=""
    if 0<=age<18:
        agestatuse="you are not allowed to work"
    elif 18<=age<60:
        agestatuse="you are in the proper age"
    elif 60<=age:
        agestatuse="you are too old to work"
    else:
        agestatuse="entered age is invalid"
    salarystatuse=""
    if 0<=salary<2000:
        salarystatuse="low income"
    elif 2000<=salary<5000:
        salarystatuse="your income is enough"
    elif 5000<=salary:
        salarystatuse="high income"
    else:
        "entered number is invalid"
    f.write(f"{name},{age},{salary},{agestatuse},{salarystatuse}\n")
f.close()