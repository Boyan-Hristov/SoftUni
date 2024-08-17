def cookbook(*args) -> str:
    result = ""
    cuisines = {}

    for el in args:
        recipe, cuisine, ingredients = el
        if cuisine not in cuisines.keys():
            cuisines[cuisine] = {}
        cuisines[cuisine][recipe] = ingredients

    cuisines = dict(sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0])))

    for current_cuisine, recipes in cuisines.items():
        result += f"{current_cuisine} cuisine contains {len(recipes)} recipes:\n"
        recipes = dict(sorted(recipes.items()))
        for current_recipe, current_ingredients in recipes.items():
            result += f"  * {current_recipe} -> Ingredients: {', '.join(current_ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))



