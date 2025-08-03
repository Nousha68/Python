a=int(input("how many students?"))
namelist=[]
scorelist=[]
for i in range(a):
    name=input("what is your name?")
    score=float(input("what is your score?"))
    namelist.append(name)
    scorelist.append(score)
print(namelist)
print(scorelist)
for i in range(a):
    print(namelist[i],scorelist[i])