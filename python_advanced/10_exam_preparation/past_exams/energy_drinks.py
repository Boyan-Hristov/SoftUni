from collections import deque

milligrams_sequence = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(y) for y in input().split(", ")])

max_caffeine = 300
total_caffeine = 0

while milligrams_sequence and energy_drinks:
    milligrams = milligrams_sequence.pop()
    drink = energy_drinks[0]
    caffeine = milligrams * drink

    if total_caffeine + caffeine <= max_caffeine:
        total_caffeine += caffeine
        energy_drinks.popleft()

    else:
        energy_drinks.append(energy_drinks.popleft())
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
