size = 6

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(size):
    matrix.append(input().split())

position = input()
row, column = int(position[1]), int(position[4])

command = input()

while "Stop" not in command:
    tokens = command.split(", ")
    operation = tokens[0]
    direction = tokens[1]

    row += directions[direction][0]
    column += directions[direction][1]

    if operation == "Create":
        value = tokens[2]
        if matrix[row][column] == ".":
            matrix[row][column] = value

    elif operation == "Update":
        value = tokens[2]
        if not matrix[row][column] == ".":
            matrix[row][column] = value

    elif operation == "Delete":
        matrix[row][column] = "."

    elif operation == "Read":
        if not matrix[row][column] == ".":
            print(matrix[row][column])

    command = input()

[print(*line) for line in matrix]
