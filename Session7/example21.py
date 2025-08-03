number=int(input("number of student"))
names=[]
for i in range(number):
    name=input("what is your name?")
    names.append(name)
print(names)
for i in names:
    print("Welcome to school", i)