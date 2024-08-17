def shop_from_grocery_list(budget: int, groceries: list, *args) -> str:
    result = ""
    bought_items = set()

    for data in args:
        product, price = data[0], float(data[1])
        if price <= budget:
            if product in groceries and product not in bought_items:
                budget -= price
                groceries.remove(product)
                bought_items.add(product)
        else:
            break

    if not groceries:
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result += f"You did not buy all the products. Missing products: " \
                  f"{', '.join(groceries)}."

    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

