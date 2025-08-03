set1={1,2,3,4,8,5}
set2={6,2,7,8}
set3={1,2,3,3,8,8,9}
set4={4,6,8,2,2,10}
a=set1.union(set2,set3,set4)
print(a)

a1=set1|set2|set3|set4
print(a1)

b=set1.intersection(set2,set3,set4)
print(b)

c=set1&set2&set3&set4
print(c)