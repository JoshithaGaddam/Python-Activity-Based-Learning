
n = int(input("Enter number of apartments: "))

apartments = []
units_list = []

for i in range(n):
    name = input("Enter apartment name: ")
    units = int(input("Enter units consumed: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    bill = bill + 50       # Fixed charge

    if units < 50:
        bill = bill - 20    # Rebate

    print(name, "Bill:", bill)

    apartments.append(name)
    units_list.append(units)

print("\nApartments ranked by consumption:")

for i in range(n):
    for j in range(i + 1, n):
        if units_list[i] < units_list[j]:
            units_list[i], units_list[j] = units_list[j], units_list[i]
            apartments[i], apartments[j] = apartments[j], apartments[i]

for i in range(n):
    print(i + 1, apartments[i], "-", units_list[i], "units")
