
days = int(input("Enter number of days: "))
limit = float(input("Enter acceptable waste percentage: "))
prepared = int(input("Enter meals prepared: "))
served = int(input("Enter meals served: "))
leftover = prepared - served
waste = (leftover / prepared) * 100

print("Leftover meals:", leftover)
print("Waste percentage:", waste, "%")

if waste > limit:
        print("High food waste!")
else:
        print("Food waste is acceptable.")
