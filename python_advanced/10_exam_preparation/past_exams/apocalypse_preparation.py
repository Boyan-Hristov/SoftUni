from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(y) for y in input().split()]

healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

created_items = {}

while textiles and medicaments:
    textile, medicament = textiles[0], medicaments[-1]
    textiles.popleft()
    if sum((textile, medicament)) in healing_items.values():
        medicaments.pop()
        item_value = sum((textile, medicament))
        for item, value in healing_items.items():
            if item_value == value:
                if item not in created_items.keys():
                    created_items[item] = 0
                created_items[item] += 1
                break

    elif sum((textile, medicament)) > healing_items["MedKit"]:
        medicaments.pop()
        if "MedKit" not in created_items.keys():
            created_items["MedKit"] = 0
        created_items["MedKit"] += 1
        remainder = sum((textile, medicament)) - healing_items["MedKit"]
        medicaments.append(medicaments.pop() + remainder)

    else:
        medicaments.append(medicaments.pop() + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if created_items:
    created_items = dict(sorted(created_items.items(), key=lambda x: (-x[1], x[0])))
    for item, count in created_items.items():
        print(f"{item} - {count}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
if medicaments:
    print(f"Medicaments left: {', '.join([str(y) for y in medicaments[::-1]])}")
