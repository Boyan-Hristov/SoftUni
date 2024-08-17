food_available = int(input())
command = input()
total_food_eaten = 0

while not command == "Adopted":
    food_eaten = int(command)
    total_food_eaten += food_eaten
    command = input()

food_available_in_grams = food_available * 1000
food_left = 0
food_needed = 0
if food_available_in_grams >= total_food_eaten:
    food_left = food_available_in_grams - total_food_eaten
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    food_needed = total_food_eaten - food_available_in_grams
    print(f"Food is not enough. You need {food_needed} grams more.")
