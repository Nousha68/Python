number=int(input("number of employees?"))
namelist=list()
salary=list()
i=0
while i<number:
    name=input("what is your name?")
    income=int(input("how much is your income?"))
    namelist.append(name)
    salary.append(income)
    i=i+1
i=0
while i<len(namelist):
    print(namelist[i],salary[i])
    i=i+1