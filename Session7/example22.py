numbers=int(input("number of courses"))
s=[]
namecourse=[]
for i in range(numbers):
    score=float(input("what is your score?"))
    s.append(score)
    name=input("which course?")
    namecourse.append(name)
print(s)
print(namecourse)
for i in range(numbers):
    if s[i]>=10:
        print("pass", s[i], namecourse[i])
    else:
        print("fail", s[i], namecourse[i])