number=int(input("tell the number of cities"))
cityname=list()
citypopulation=list()
for i in range(number):
    city=input("what is the city name?")
    population=int(input("how much is the population?"))
    cityname.append(city)
    citypopulation.append(population)
for i in range(len(cityname)):
    print(cityname[i],citypopulation[i])