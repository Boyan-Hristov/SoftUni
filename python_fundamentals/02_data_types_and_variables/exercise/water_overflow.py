tank_capacity = 255
number_of_lines = int(input())
liters_added = 0
for line in range(number_of_lines):
    liters_of_water = int(input())
    if tank_capacity < liters_of_water:
        print("Insufficient capacity!")
        continue
    else:
        tank_capacity -= liters_of_water
        liters_added += liters_of_water
print(liters_added)