size = int(input())

matrix = []
starting_position = []
final_positions = []
max_eggs = float("-inf")
best_direction = ""

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(size):
    row = input().split()
    matrix.append(row)
    for j in range(size):
        if matrix[i][j] == "B":
            starting_position = [i, j]


for move, steps in directions.items():
    starting_row, starting_column = starting_position[0], starting_position[1]
    row, column = starting_row + steps[0], starting_column + steps[1]

    eggs_collected = 0
    positions = []

    while row in range(size) and column in range(size):
        target_position = matrix[row][column]
        if target_position == "X":
            break
        else:
            eggs_collected += int(target_position)
            positions.append([row, column])
        row += steps[0]
        column += steps[1]

    if eggs_collected >= max_eggs:
        max_eggs = eggs_collected
        best_direction = move
        final_positions = positions

print(best_direction)
[print(row) for row in final_positions]
print(max_eggs)
