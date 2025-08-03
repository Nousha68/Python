import numpy as np
number=int(input("the number of players?"))
namelist=[]
for i in range(number):
    name=input("what is the name of player?")
    namelist.append(name)
winner=int(input("how many winners?"))
a=np.random.choice(namelist,winner)
print(a)