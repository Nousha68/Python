set1={1,2,3,4,8,5}
set2={6,2,7,8}
set3={1,2,3,3,8,8,9}
set4={4,6,8,2,2,10}

set1.update(set2,set3,set4)
print(set1)

set1.intersection_update(set2,set3,set4)
print(set1)