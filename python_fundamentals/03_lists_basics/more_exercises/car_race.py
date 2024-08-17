time_controls = input().split()
half_controls = len(time_controls) // 2
first_car_time_controls = time_controls[:half_controls]
second_car_time_controls = time_controls[half_controls + 1:]
second_car_time_controls = second_car_time_controls[::-1]

left_car_total_time = 0
for time in first_car_time_controls:
    if time == "0":
        left_car_total_time *= 0.8
    left_car_total_time += int(time)

right_car_total_time = 0
for time in second_car_time_controls:
    if time == "0":
        right_car_total_time *= 0.8
    right_car_total_time += int(time)

if left_car_total_time < right_car_total_time:
    print(f"The winner is left with total time: {left_car_total_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_total_time:.1f}")