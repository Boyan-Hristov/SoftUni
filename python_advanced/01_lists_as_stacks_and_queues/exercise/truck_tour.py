from collections import deque

petrol_pumps = int(input())
queue = deque()

for pump in range(petrol_pumps):
    petrol, distance = [int(digit) for digit in input().split()]
    queue.append({"petrol": petrol, "distance": distance})

first_possible_pump = 0

for pump in range(petrol_pumps):
    current_queue = queue.copy()
    current_queue.rotate(- pump)
    petrol_in_tank = 0
    counter = 0
    for i in range(len(current_queue)):
        counter += 1
        current_pump = current_queue.popleft()
        petrol_in_tank += current_pump["petrol"]
        petrol_in_tank -= current_pump["distance"]
        if petrol_in_tank < 0:
            petrol_in_tank = 0
            break
    first_possible_pump = pump
    if counter == petrol_pumps:
        break

print(first_possible_pump)
