num=int(input("number of products?"))
f=open("products.csv","w")
for i in range(num):
    name=input("products name?")
    f.write(name+"\n")
f.close()