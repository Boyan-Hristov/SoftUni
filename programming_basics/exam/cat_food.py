cats = int(input())

food_price = 12.45

small_cats = 0
big_cats = 0
huge_cats = 0
total_food = 0

for _ in range(cats):
    food_quantity = float(input())
    if 100 <= food_quantity < 200:
        small_cats += 1
    elif food_quantity < 300:
        big_cats += 1
    elif food_quantity < 400:
        huge_cats += 1
    total_food += food_quantity

total_food_in_kg = total_food / 1000
total_food_cost = total_food_in_kg * food_price

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_food_cost:.2f} lv.")