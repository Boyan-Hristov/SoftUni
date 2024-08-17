number_of_snowballs = int(input())
max_weight = 0
best_time = 0
max_quality = 0
max_value = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / time_needed) ** snowball_quality
    if snowball_value > max_value:
        max_value = int(snowball_value)
        max_weight = snowball_weight
        best_time = time_needed
        max_quality = snowball_quality
print(f"{max_weight} : {best_time} = {max_value} ({max_quality})")
