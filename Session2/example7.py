name1=input("what is your name?")
h1=float(input("what is your height?"))
w1=float(input("how much is your weight?"))
name2=input("what is your name?")
h2=float(input("what is your height?"))
w2=float(input("how much is your weight?"))
bmi1=w1/(h1**2)
bmi2=w2/(h2**2)
if bmi1 <=1 or bmi2 <=1:
    print("numbers are invalid")
else:
    if bmi1==bmi2:
        print(name1 + " and " + name2 + " bmi is equal ")
    elif bmi1>bmi2:
        print(name1 + " is " + str(bmi1-bmi2) + " has more wight than " + name2)
    elif bmi1<bmi2:
        print(name2 + "is " + str(bmi2-bmi1) + " has less weight than " + name1)

