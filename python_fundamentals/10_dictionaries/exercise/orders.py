command = input()
products = {}
while command != "buy":
    name, price, quantity = command.split()
    if name not in products.keys():
        products[name] = {"price": float(price), "quantity": float(quantity)}
    else:
        products[name]["price"] = float(price)
        products[name]["quantity"] += float(quantity)
    command = input()
for product, info in products.items():
    total_price = info["price"] * info["quantity"]
    print(f"{product} -> {total_price:.2f}")
