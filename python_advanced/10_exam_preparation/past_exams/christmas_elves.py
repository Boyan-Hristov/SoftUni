from collections import deque

elves_energy = deque([int(x) for x in input().split()])
boxes = [int(y) for y in input().split()]

energy_used = 0
toys = 0
counter = 0

while elves_energy and boxes:
    energy = elves_energy.popleft()
    materials = boxes.pop()
    toys_made = 0

    if energy < 5:
        boxes.append(materials)
        continue

    counter += 1

    if counter % 3 == 0:
        if energy >= materials * 2:
            toys_made = 2
            toys += toys_made
            energy_used += materials * 2
            energy -= materials * 2

    else:
        if energy >= materials:
            toys_made = 1
            toys += toys_made
            energy_used += materials
            energy -= materials

    if toys_made:
        if counter % 5 == 0:
            toys -= toys_made
            elves_energy.append(energy)
        else:
            elves_energy.append(energy + 1)
    else:
        elves_energy.append(energy * 2)
        boxes.append(materials)

print(f"Toys: {toys}")
print(f"Energy: {energy_used}")
if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
if boxes:
    print(f"Boxes left: {', '.join([str(y) for y in boxes])}")
