a=int(input(" number 1 "))
if a%2==0:
    for i in range(0,a):
        print(i**2)
elif a%3==0:
    for i in range(0,a):
        print(i**3)
elif a%5==0:
    for i in range(0,a):
        print(i**5)
else:
    for i in range(a):
        print(i)