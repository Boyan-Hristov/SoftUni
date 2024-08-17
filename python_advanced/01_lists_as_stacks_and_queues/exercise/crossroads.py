from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
command = input()

queue = deque()
is_crash = False
cars_in_intersection = deque()
cars_passed = 0
time_remaining = 0

while not command == "END":
    if command == "green":
        time_remaining = green_light_duration
        while queue:
            current_car = queue.popleft()
            cars_in_intersection.append(current_car)
            time_remaining -= len(current_car)
            if time_remaining > 0:
                cars_in_intersection.popleft()
                cars_passed += 1
            else:
                time_remaining += free_window_duration
                if time_remaining >= 0:
                    if cars_in_intersection:
                        cars_in_intersection.clear()
                        cars_passed += 1
                    break
                else:
                    is_crash = True
                    character_hit_index = time_remaining
    else:
        queue.append(command)
    if is_crash:
        break
    command = input()

if is_crash:
    car_crashed = cars_in_intersection.popleft()
    print("A crash happened!")
    print(f"{car_crashed} was hit at {car_crashed[time_remaining]}.")
else:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
