set1={1,2,3,4,8,5}
set2={6,7}
set3={1,2,3,3,8,8,9}
set4={4,6,8,2,2,7,10}
a=set2.issubset(set4)
print(a)
b=set3.issubset(set1)
print(b)
c=set4.issuperset(set2)
print(c)
d=set2.isdisjoint(set3)
print(d)
for i in set4:
    print(i,end="\t")
print()
for i in range(len(set4)):
    print(i)
print("%"*50)
print(len(set4))
