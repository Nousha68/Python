a=int(input("number1 "))
b=int(input("number2 "))
for X in range(a,b):
    if X%2==0:
        print(X, "2 divide")
    elif X%5==0:
        print(X, "5 divide")
    elif X%3==0:
        print(X, "3 divide")
