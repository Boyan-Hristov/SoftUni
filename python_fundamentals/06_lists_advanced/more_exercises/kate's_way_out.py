number_of_rows = int(input())
maze = []
for row in range(number_of_rows):
    current_row = input()
    maze.append(current_row)
kate_position_in_row = 0
kate_row = 0
for element in maze:
    if "k" in element:
        kate_position = element.index("k")
        kate_row = element
for current_element in maze:
    if " " in current_element:
        pass

