def stock_availability(inventory: list, action: str, *args) -> list:
    if action == "delivery":
        for el in args:
            inventory.append(el)
    elif action == "sell":
        if not args:
            inventory.pop(0)
        else:
            if isinstance(args[0], int):
                for i in range(int(args[0])):
                    if inventory:
                        inventory.pop(0)
            else:
                for el in args:
                    for i in range(len(inventory) - 1, -1, -1):
                        if inventory[i] == el:
                            inventory.remove(el)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
