stock = {}
command = input().split(": ")
while command[0] != "statistics":
    product = command[0]
    quantity = command[1]
    if product not in stock.keys():
        stock[product] = int(quantity)
    else:
        stock[product] += int(quantity)
    command = input().split(": ")
print("Products in stock:")
for (product, quantity) in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")
