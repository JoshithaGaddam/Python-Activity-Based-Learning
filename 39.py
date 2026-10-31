
attendance = int(input("Enter attendance percentage: "))
lab = input("Lab completed? (yes/no): ")
internal = int(input("Enter internal marks: "))
fees = input("Fees paid? (yes/no): ")

eligible = True

if attendance < 75:
    print("Insufficient attendance")
    eligible = False

if lab != "yes":
    print("Lab not completed")
    eligible = False

if internal < 40:
    print("Internal marks are insufficient")
    eligible = False

if fees != "yes":
    print("Fees not cleared")
    eligible = False

if eligible:
    print("Eligible for final examination")
else:
    print("Not eligible for final examination")
