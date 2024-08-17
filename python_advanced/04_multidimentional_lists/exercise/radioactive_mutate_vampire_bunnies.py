from collections import deque

size = [int(x) for x in input().split()]
rows = size[0]
columns = size[1]

matrix = []

starting_position = []
bunnies = []

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

for i in range(rows):
    data = list(input())
    matrix.append(data)
    for j in range(len(data)):
        if data[j] == "P":
            starting_position.extend([i, j])
        elif data[j] == "B":
            bunny = [i, j]
            bunnies.append(bunny)

commands = deque(input())

row, column = starting_position[0], starting_position[1]

while commands:
    matrix[row][column] = "."
    command = commands.popleft()
    row += directions[command][0]
    column += directions[command][1]

    new_bunnies = []

    for rabbit in bunnies:
        r, c = rabbit[0], rabbit[1]
        if r - 1 in range(rows):
            matrix[r - 1][c] = "B"
            new_bunnies.append([r - 1, c])
        if r + 1 in range(rows):
            matrix[r + 1][c] = "B"
            new_bunnies.append([r + 1, c])
        if c - 1 in range(columns):
            matrix[r][c - 1] = "B"
            new_bunnies.append([r, c - 1])
        if c + 1 in range(columns):
            matrix[r][c + 1] = "B"
            new_bunnies.append([r, c + 1])

    for new_bunny in new_bunnies:
        bunnies.append(new_bunny)

    if row in range(rows) and column in range(columns):
        target_position = matrix[row][column]

    else:
        row -= directions[command][0]
        column -= directions[command][1]
        matrix[row][column] = "."
        for line in matrix:
            print("".join(line))
        print(f"won: {row} {column}")
        break

    if matrix[row][column] == "B":
        for line in matrix:
            print("".join(line))
        print(f"dead: {row} {column}")
        break
