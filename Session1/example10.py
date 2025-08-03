
w=float(input("weight:"))
h=float(input("height:"))
bmi=w/(h**2)
print("bmi=", bmi)
if 0<bmi<18:
   print("too thin")
elif 18<=bmi<24.9:
   print("normal")
elif 24.9<=bmi<29.9:
   print("extra weight")
elif 29.9<=bmi<34.9:
   print("fat 1")
elif 34.9<=bmi:
   print("fat 2")
else:
   print("you entered wrong number for w or h")

