number=int(input("number of employees?"))
namelist=list()
salary=list()
for i in range(number):
    name=input("what is your name?")
    income=int(input("how much is your income?"))
    namelist.append(name)
    salary.append(income)
for i in range(len(namelist)):
    print(namelist[i],salary[i])

