key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
key_materials_needed = 250
item_obtained = ""
while item_obtained == "":
    materials = input().split()
    for i in range(0, len(materials), 2):
        key = materials[i + 1].lower()
        value = int(materials[i])
        if key == "shards" or key == "fragments" or key == "motes":
            key_materials[key] += value
            if key_materials[key] >= key_materials_needed:
                key_materials[key] -= key_materials_needed
                if key == "shards":
                    item_obtained = "Shadowmourne"
                elif key == "fragments":
                    item_obtained = "Valanyr"
                elif key == "motes":
                    item_obtained = "Dragonwrath"
                break
        else:
            if key in junk.keys():
                junk[key] += value
            else:
                junk[key] = value

print(f"{item_obtained} obtained!")
for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
for item, count in junk.items():
    print(f"{item}: {count}")
