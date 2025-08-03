number=int(input("number of employees?"))
namelist=list()
salary=list()
for i in range(number):
    name=input("what is your name?")
    income=int(input("how much is your income?"))
    namelist.append(name)
    salary.append(income)
X=0
while X<len(namelist):
    print(namelist[X],salary[X])
    X=X+1