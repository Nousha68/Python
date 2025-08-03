number=int(input("number of courses?"))
coursenames=list()
coursescores=list()
for i in range(number):
    name=input("what is the course name?")
    score=float(input("what is the course score?"))
    coursenames.append(name)
    coursescores.append(score)
print(coursenames)
print(coursescores)
for i in range(len(coursenames)):
    print(coursenames[i], coursescores[i])

