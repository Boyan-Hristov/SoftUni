def shopping_cart(*args) -> str:
    result = ""
    meals = {
        "Soup": set(),
        "Pizza": set(),
        "Dessert": set()
    }
    meals_capacity = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }

    for data in args:
        if data == "Stop":
            break

        meal, product = data
        if len(meals[meal]) < meals_capacity[meal]:
            meals[meal].add(product)

    meals = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in meals.items():
        result += f"{key}:\n"
        value = list(sorted(value))
        for item in value:
            result += f" - {item}\n"

    total_items = sum({len(items) for items in meals.values()})
    if total_items == 0:
        result = "No products in the cart!"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))




