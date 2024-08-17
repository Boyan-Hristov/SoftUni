from collections import deque

presents_magic_needed = {
    150: "doll",
    250: "wooden train",
    300: "teddy bear",
    400: "bicycle"
}

boxes = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {}

while boxes and magic_levels:
    materials = boxes.pop()
    magic = magic_levels.popleft()
    if materials == 0 or magic == 0:
        if materials != 0:
            boxes.append(materials)
        if magic != 0:
            magic_levels.appendleft(magic)
        continue

    total_magic = materials * magic
    if total_magic < 0:
        new_materials = materials + magic
        boxes.append(new_materials)
    else:
        if total_magic in presents_magic_needed.keys():
            present = presents_magic_needed[total_magic]
            if present not in presents.keys():
                presents[present] = 0
            presents[present] += 1
        else:
            boxes.append(materials + 15)

is_doll = False
is_train = False
is_bear = False
is_bicycle = False

for name in presents.keys():
    if name == "doll":
        is_doll = True
    elif name == "wooden train":
        is_train = True
    elif name == "teddy bear":
        is_bear = True
    elif name == "bicycle":
        is_bicycle = True

if (is_doll and is_train) or (is_bear and is_bicycle):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print("Materials left: ", end="")
    print(*boxes[::-1], sep=", ")
if magic_levels:
    print("Magic left: ", end="")
    print(*magic_levels, sep=", ")

presents = dict(sorted(presents.items()))
for key, value in presents.items():
    print(f"{key.capitalize()}: {value}")
