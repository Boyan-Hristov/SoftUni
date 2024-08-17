animals = {}
areas = {}
animals_fed = []
command = input()
while not command == "EndDay":
    command_info = command.split(": ")
    action = command_info[0]
    animal_info = command_info[1].split("-")
    if action == "Add":
        animal, food_needed, area = animal_info[0], int(animal_info[1]), animal_info[2]
        if animal not in animals.keys():
            animals[animal] = 0
        animals[animal] += food_needed
        if area not in areas.keys():
            areas[area] = []
        if animal not in areas[area]:
            areas[area].append(animal)
    elif action == "Feed":
        name, food = animal_info[0], int(animal_info[1])
        if name in animals.keys():
            animals[name] -= food
            if animals[name] <= 0:
                animals.pop(name)
                animals_fed.append(name)
                print(f"{name} was successfully fed")
    command = input()

for area, residents in areas.items():
    for current_animal in animals_fed:
        if current_animal in residents:
            residents.remove(current_animal)

print("Animals:")
for animal_name, needed_food in animals.items():
    print(f" {animal_name} -> {needed_food}g")

print("Areas with hungry animals:")
for area_name, hungry_animals in areas.items():
    if hungry_animals:
        print(f" {area_name}: {len(hungry_animals)}")
