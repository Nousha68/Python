set1={1,2,3,4,8,5}
set2={6,2,7,8}
set3={1,2,3,3,8,8,9}
set4={4,6,8,2,2,10}
a=set1.difference(set2,set3,set4)
print(a)

a1=set1-set2-set3-set4
print(a1)

b=set1.symmetric_difference(set2)
print(b)
b1=set1^set2
print(b1)
b2=set1^set2^set3^set4
print(b2)