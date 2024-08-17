size = int(input())

matrix = []
tea_bags = 0
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
            matrix[i][j] = "*"

while tea_bags < 10:
    command = input()
    row += directions[command][0]
    column += directions[command][1]

    if row not in range(size) or column not in range(size):
        break

    if matrix[row][column] == "R":
        matrix[row][column] = "*"
        break

    if matrix[row][column].isdigit():
        tea_bags += int(matrix[row][column])

    matrix[row][column] = "*"

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
