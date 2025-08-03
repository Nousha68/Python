class1=int(input("how many students are in Math class?"))
mathclass=set()
for i in range(class1):
    name=input("what are their names?")
    mathclass.add(name)
class2=int(input("how many students are in geography class?"))
geoclass=set()
for i in range(class2):
    name=input("what are their names?")
    geoclass.add(name)
a=mathclass.intersection(geoclass)
b=geoclass-mathclass
c=mathclass-geoclass
print("students are in both class"+str(a))
print("student are in mathclass"+ str(b))
print("student are in geoclass"+ str(c))
