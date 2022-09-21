# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92

items = int(input("Number of items: "))
total_price = 0
discount = 0.9
while items <= 0:
    print("Invalid item amounts, please enter a valid amount")
    items = float(input("Number of items: "))

for i in range(items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    discount_price = discount * total_price
    print("Total price for {} items is ${:.2f} with a 10% discount"
          .format(items, discount_price))
else:
    print("Total price for {} items is ${:.2f}".format(items, total_price))


