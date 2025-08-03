name=input("tell me your name?")
age=int(input("tell me your age?"))
score=float(input("tell me your score?"))
print(name, age, score)
print(name+str(age)+str(score))

if age>18:
    print("adult")
else:
    print("young")

if 0<=score<10:
    print("fail")
elif 10<=score<15:
    print("normal")
elif 15<=score<20:
    print("pass")

for i in range(1,age+1):
    print("*"*i)