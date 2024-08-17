treasure_chest = input().split("|")

while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    elif action == "Loot":
        loot = command.copy()
        loot.remove("Loot")
        for item in loot:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif action == "Drop":
        index = int(command[1])
        if 0 <= index < len(treasure_chest):
            item_to_remove = treasure_chest[index]
            treasure_chest.remove(item_to_remove)
            treasure_chest.append(item_to_remove)
    elif action == "Steal":
        count = int(command[1])
        stolen_items = []
        if count >= len(treasure_chest):
            stolen_items = treasure_chest.copy()
            treasure_chest = []
        else:
            for index in range(len(treasure_chest) - 1, - 1, -1):
                if len(stolen_items) < count:
                    stolen_items.insert(0, treasure_chest[index])
                    treasure_chest.pop(index)
                else:
                    break
        print(", ".join(stolen_items))

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    items_sum = 0
    for item in treasure_chest:
        items_sum += len(item)
    average_gain = items_sum / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

