directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())
matrix = []
moves = input().split(", ")
starting_position = []

for i in range(size):
    line = list(input())
    matrix.append(line)
    if "s" in line:
        starting_position = [i, line.index("s")]
        matrix[i][line.index("s")] = "*"

row, column = starting_position
nuts_collected = 0

for move in moves:
    row += directions[move][0]
    column += directions[move][1]

    if row not in range(size) or column not in range(size):
        print("The squirrel is out of the field.")
        break

    if matrix[row][column] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    elif matrix[row][column] == "h":
        nuts_collected += 1
        matrix[row][column] = "*"
        if nuts_collected == 3:
            print("Good job! You have collected all hazelnuts!")
            break

else:
    if nuts_collected < 3:
        print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {nuts_collected}")
