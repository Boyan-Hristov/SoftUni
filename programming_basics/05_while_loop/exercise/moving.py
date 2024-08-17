width = int(input())
length = int(input())
height = int(input())

free_area = width * length * height

command = input()
boxes_moved = 0
is_full = False

while not command == "Done":
    current_boxes = int(command)
    boxes_moved += current_boxes
    if boxes_moved > free_area:
        is_full = True
        break
    command = input()

space_needed = 0
space_left = 0
if is_full:
    space_needed = boxes_moved - free_area
    print(f"No more free space! You need {space_needed} Cubic meters more.")
else:
    space_left = free_area - boxes_moved
    print(f"{space_left} Cubic meters left.")