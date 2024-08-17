# import re
#
# food_items = []
# total_calories = 0
# calories_needed_per_day = 2000
# food_info = input()
# pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
# match = re.findall(pattern, food_info)
#
# for food in match:
#     food_name = food[1]
#     expiration_date = food[2]
#     calories = int(food[3])
#     food_item = {"name": food_name, "expiration date": expiration_date, "calories": calories}
#     food_items.append(food_item)
#     total_calories += calories
#
# days_to_last = total_calories // calories_needed_per_day
# print(f"You have food to last you for: {days_to_last} days!")
# for item in food_items:
#     print(f"Item: {item['name']}, Best before: {item['expiration date']}, Nutrition: {item['calories']}")


import re

total_calories = 0
calories_needed_per_day = 2000
food_info = input()
pattern = r"([\|#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.findall(pattern, food_info)
for item in matches:
    total_calories += int(item[3])
days_with_food = total_calories // calories_needed_per_day
print(f"You have food to last you for: {days_with_food} days!")
for item in matches:
    print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {int(item[3])}")
