name1=input("name player 1")
h1=float(input("height player 1"))
name2=input("name player 2")
h2=float(input("height player 2"))
if h1==h2:
    print(name1 + " and "+ name2 + " height is equal")
elif h1>h2:
    print(name1 +" is "+str(h1-h2)+" higher than "+ name2)
else:
    print(name2 + " is " + str(h2-h1)+ " higher than " + name1)
