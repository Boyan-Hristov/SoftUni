from math import ceil
from math import floor

days = int(input())
food_available = int(input())
dog_ration_per_day_in_kilograms = float(input())
cat_ration_per_day_in_kilograms = float(input())
turtle_ration_per_day_in_grams = float(input())

turtle_ration_per_day_in_kilograms = turtle_ration_per_day_in_grams / 1000

food_eaten = dog_ration_per_day_in_kilograms * days \
    + cat_ration_per_day_in_kilograms * days \
    + turtle_ration_per_day_in_kilograms * days

food_left = 0
food_needed = 0
if food_available > food_eaten:
    food_left = food_available - food_eaten
    print(f"{floor(food_left)} kilos of food left.")
else:
    food_needed = food_eaten - food_available
    print(f"{ceil(food_needed)} more kilos of food are needed.")