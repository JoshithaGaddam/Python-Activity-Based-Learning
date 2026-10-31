n = int(input("Enter number of areas: "))

areas = []
demand = []
supply = []

for i in range(n):
    area = input("Enter area name: ")
    d = int(input("Enter water demand: "))
    s = int(input("Enter water supply: "))

    areas.append(area)
    demand.append(d)
    supply.append(s)

shortages = []

for i in range(n):
    shortage = max(0, demand[i] - supply[i])
    shortages.append(shortage)
    print(areas[i], "Shortage:", shortage)

index = shortages.index(max(shortages))
print("Most underserved area:", areas[index])