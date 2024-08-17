size = 5

matrix = []
targets = []
targets_hit = []

row = 0
column = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(size):
    data = input().split()
    matrix.append(data)

    for j in range(size):
        if matrix[i][j] == "A":
            row, column = i, j
            matrix[i][j] = "."
        elif matrix[i][j] == "x":
            targets.append((i, j))

for _ in range(int(input())):
    tokens = input().split()
    command = tokens[0]
    if command == "shoot":
        direction = tokens[1]
        x, y = row, column
        x += directions[direction][0]
        y += directions[direction][1]

        while x in range(size) and y in range(size):
            if matrix[x][y] == "x":
                targets_hit.append([x, y])
                matrix[x][y] = "."
                break
            x += directions[direction][0]
            y += directions[direction][1]

        if len(targets) == len(targets_hit):
            print(f"Training completed! All {len(targets)} targets hit.")
            break

    elif command == "move":
        direction = tokens[1]
        steps = int(tokens[2])

        row += directions[direction][0] * steps
        column += directions[direction][1] * steps
        if row in range(size) and column in range(size):
            if matrix[row][column] == "x":
                row -= directions[direction][0]
                column -= directions[direction][1]
        else:
            row -= directions[direction][0] * steps
            column -= directions[direction][1] * steps

if not len(targets) == len(targets_hit):
    print(f"Training not completed! {len(targets) - len(targets_hit)} targets left.")
if targets_hit:
    [print(row) for row in targets_hit]
