def shopping_list(budget: int, **kwargs) -> str:
    result = ""
    if budget < 100:
        return "You do not have enough budget."
    products_bought = 0

    for key, value in kwargs.items():
        product = key
        price, quantity = value
        if budget >= price * quantity and products_bought < 5:
            budget -= price * quantity
            products_bought += 1
            result += f"You bought {product} for {price * quantity:.2f} leva.\n"

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))




