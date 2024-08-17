rows, columns = [int(x) for x in input().split(",")]
matrix = []
starting_position = []
cheese_count = 0

for i in range(rows):
    line = list(input())
    matrix.append(line)
    if "M" in line:
        starting_position = [i, line.index("M")]
    elif "C" in line:
        cheese_count += line.count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, column = starting_position
matrix[row][column] = "*"
command = input()

while not command == "danger":
    row += directions[command][0]
    column += directions[command][1]

    if row not in range(rows) or column not in range(columns):
        row -= directions[command][0]
        column -= directions[command][1]
        print("No more cheese for tonight!")
        break

    if matrix[row][column] == "C":
        cheese_count -= 1
        matrix[row][column] = "*"
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[row][column] == "T":
        print("Mouse is trapped!")
        break

    elif matrix[row][column] == "@":
        row -= directions[command][0]
        column -= directions[command][1]

    command = input()

matrix[row][column] = "M"

if command == "danger" and cheese_count > 0:
    print("Mouse will come back later!")
[print(*line, sep="") for line in matrix]
