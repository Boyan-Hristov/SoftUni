from collections import deque

gifts = {
    "Gemstone": range(100, 200),
    "Porcelain Sculpture": range(200, 300),
    "Gold": range(300, 400),
    "Diamond Jewellery": range(400, 500)
}

gifts_made = {}

materials = [int(x) for x in input().split()]
magic_levels = deque([int(y) for y in input().split()])

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    result = material + magic

    if result in range(100, 500):
        for gift, magic_needed in gifts.items():
            if result in magic_needed:
                if gift not in gifts_made.keys():
                    gifts_made[gift] = 0
                gifts_made[gift] += 1
                break
    else:
        if result < 100:
            if result % 2 == 0:
                material *= 2
                magic *= 3
                result = material + magic
            else:
                result *= 2
        elif result > 499:
            result /= 2

        if result in range(100, 500):
            for gift, magic_needed in gifts.items():
                if result in magic_needed:
                    if gift not in gifts_made.keys():
                        gifts_made[gift] = 0
                    gifts_made[gift] += 1
                    break

if ("Gemstone" in gifts_made.keys() and "Porcelain Sculpture" in gifts_made.keys()) or \
        ("Gold" in gifts_made.keys() and "Diamond Jewellery" in gifts_made.keys()):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(y) for y in magic_levels])}")

gifts_made = dict(sorted(gifts_made.items(), key=lambda x: x[0]))
for key, value in gifts_made.items():
    print(f"{key}: {value}")
