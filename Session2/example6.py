name=input("what is your name?")
h=float(input("what is your height?"))
w=float(input("how much is your weight?"))
bmi=w/(h**2)
print("bmi=" + str(bmi))
if bmi<18:
    print(name + " is too thin")
elif 18<=bmi<24.9:
    print(name + " is normal")
elif 24.9<=bmi<29.9:
    print(name + " is extra weight")
elif 29.9<=bmi<34.9:
    print(name + " is fat 1")
elif 34.9<=bmi:
    print(name + " is fat 2")
else:
    print(" weight or height is not valid")
