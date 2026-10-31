
stock = 50
price = 30
sales = 0

n = int(input("Enter number of orders: "))

for i in range(n):
    qty = int(input("Enter order quantity: "))

    if qty <= 0:
        print("Invalid quantity")

    elif qty > stock:
        print("Not enough stock")

    else:
        bill = qty * price
        stock = stock - qty
        sales = sales + bill

        print("Bill amount:", bill)

print("\nDaily Summary")
print("Total Sales:", sales)
print("Remaining Stock:", stock)
