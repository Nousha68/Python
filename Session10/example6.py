num=int(input("how many suppliers?"))
supplier=set()
for i in range(num):
    name=input("what is the name of supplier").strip()
    supplier.add(name)
num2=int(input("how many customers?"))
customer=set()
for i in range(num2):
    name=input("what is the name of customer?").strip()
    customer.add(name)
a=supplier.intersection(customer)
print(a)