items = input()
budget = float(input())

items_list = items.split("|")

clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
train_ticket_price = 150

money_spent = 0
new_prices = []

for item in items_list:
    item_info = item.split("->")
    if float(item_info[1]) <= budget:
        if item_info[0] == "Clothes":
            if float(item_info[1]) <= 50.00:
                budget -= float(item_info[1])
                money_spent += float(item_info[1])
                new_prices.append(float(item_info[1]) * 1.4)
        elif item_info[0] == "Shoes":
            if float(item_info[1]) <= 35.00:
                budget -= float(item_info[1])
                money_spent += float(item_info[1])
                new_prices.append(float(item_info[1]) * 1.4)
        elif item_info[0] == "Accessories":
            if float(item_info[1]) <= 20.50:
                budget -= float(item_info[1])
                money_spent += float(item_info[1])
                new_prices.append(float(item_info[1]) * 1.4)

for price in new_prices:
    budget += price
    print(f"{price:.2f}", end=" ")
print()
profit = sum(new_prices) - money_spent
print(f"Profit: {profit:.2f}")
if budget >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")