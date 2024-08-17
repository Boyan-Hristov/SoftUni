directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

rows, columns = [int(x) for x in input().split()]
matrix = []
starting_position = []

for i in range(rows):
    line = list(input())
    matrix.append(line)
    if "B" in line:
        starting_position = [i, line.index("B")]

row, column = starting_position[0], starting_position[1]

while True:
    command = input()
    row += directions[command][0]
    column += directions[command][1]

    if row not in range(rows) or column not in range(columns):
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[row][column] == "*":
        row -= directions[command][0]
        column -= directions[command][1]

    elif matrix[row][column] == "-":
        matrix[row][column] = "."

    elif matrix[row][column] == "P":
        matrix[row][column] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[row][column] == "A":
        matrix[row][column] = "P"
        print("Pizza is delivered on time! Next order...")
        break

[print(*line, sep="") for line in matrix]
