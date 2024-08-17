text = list(input())
size = int(input())

matrix = []
position = []

for i in range(size):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        position = [i, line.index("P")]
        matrix[i][line.index("P")] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

commands_count = int(input())
row, col = position

for j in range(commands_count):
    direction = input()
    row += directions[direction][0]
    col += directions[direction][1]

    if row in range(size) and col in range(size):
        if matrix[row][col].isalpha():
            text.append(matrix[row][col])
            matrix[row][col] = "-"
    else:
        if text:
            text.pop()
            row -= directions[direction][0]
            col -= directions[direction][1]

matrix[row][col] = "P"

print(*text, sep="")
[print(*line, sep="") for line in matrix]
