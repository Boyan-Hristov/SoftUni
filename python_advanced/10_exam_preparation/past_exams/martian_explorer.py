size = 6

rover_position = []
deposits_found = set()

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

deposits = {
    "W": "Water deposit",
    "M": "Metal deposit",
    "C": "Concrete deposit"
}

for i in range(size):
    row = input().split()
    matrix.append(row)
    for j in range(size):

        if matrix[i][j] == "E":
            rover_position = [i, j]
            matrix[i][j] = "-"

commands = input().split(", ")

row, column = rover_position[0], rover_position[1]

for command in commands:
    row += directions[command][0]
    column += directions[command][1]

    if row not in range(size):
        if command == "up":
            row = 5
        elif command == "down":
            row = 0
    elif column not in range(size):
        if command == "left":
            column = 5
        elif command == "right":
            column = 0

    if matrix[row][column] == "R":
        print(f"Rover got broken at ({row}, {column})")
        break

    elif matrix[row][column] == "W" or \
            matrix[row][column] == "M" or \
            matrix[row][column] == "C":
        deposit = matrix[row][column]
        matrix[row][column] = "-"
        deposits_found.add(deposit)
        print(f"{deposits[deposit]} found at ({row}, {column})")

if len(deposits_found) < 3:
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")
