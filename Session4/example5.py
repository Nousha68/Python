a=int(input("how many employee do you have?"))
salarylist=[]
for i in range(a):
    salary=float(input("how much is your salary?"))
    salarylist.append(salary)
print(salarylist)
for i in salarylist:
    if i>=2000:
        print(i,"is enough salary")
    else:
        print(i,"is low income")
