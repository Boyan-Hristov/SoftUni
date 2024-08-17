floors_count = int(input())
rooms_count = int(input())

designation = ""

for current_floor in range(floors_count, 0, -1):
    if current_floor == floors_count:
        designation = "L"
    elif current_floor % 2 == 0:
        designation = "O"
    elif current_floor % 2 != 0:
        designation = "A"
    for current_room in range(rooms_count):
        print(f"{designation}{current_floor}{current_room} ", end = "")
    print()
