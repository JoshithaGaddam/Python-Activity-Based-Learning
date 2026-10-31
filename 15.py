print("Parking Charge Calculator")

vehicle = input("Enter vehicle type (car/bike): ")
entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")

elif vehicle != "car" and vehicle != "bike":
    print("Invalid vehicle type")

else:
    if exit < entry:
        hours = exit + 24 - entry
    else:
        hours = exit - entry

    if vehicle == "car":
        rate = 30
    else:
        rate = 15

    charge = hours * rate

    if hours > 12:
        charge = charge + 100

    if charge > 300:
        charge = 300

    print("Parking hours:", hours)
    print("Total parking charge: Rs.", charge)