a="Mehrnoosh Mln"
print(a)
print(type(a))
print(a[0])
print(a[0:9])
print(a[0:])
b="""Today is rainy
   Tomorrow is sunny
   
   yesterday was windy"""
print(b)
a=a.lower()
print(a)
a=b.upper()
print(a)
print("$$$"*20)
for i in "Mehrnoosh":
    print(i)

print("$$$" * 20)
import time
for i in a:
    time.sleep(0.1)
    print(i,end="")
print()
for i in a:
    time.sleep(0.1)
    print(i,end="\t")