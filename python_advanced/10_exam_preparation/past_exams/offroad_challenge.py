from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_indices = deque([int(y) for y in input().split()])
altitudes = deque([int(z) for z in input().split()])

is_interrupted = False
target = len(altitudes)
altitude_reached = 0
altitudes_reached = []

while altitudes:
    fuel_available = initial_fuel.pop()
    added_consumption = consumption_indices.popleft()
    fuel_needed = altitudes.popleft()

    if fuel_available - added_consumption >= fuel_needed:
        altitude_reached += 1
        altitudes_reached.append(f"Altitude {altitude_reached}")
        print(f"John has reached: Altitude {altitude_reached}")

    else:
        is_interrupted = True
        print(f"John did not reach: Altitude {altitude_reached + 1}")
        break

if is_interrupted:
    print("John failed to reach the top.")
    if altitude_reached > 0:
        print(f"Reached altitudes: {', '.join(altitudes_reached)}")
    else:
        print("John didn't reach any altitude.")
if altitude_reached == target:
    print(f"John has reached all the altitudes and managed to reach the top!")
