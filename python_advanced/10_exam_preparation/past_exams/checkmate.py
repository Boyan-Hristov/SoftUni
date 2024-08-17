size = 8
matrix = []
queens = []

for i in range(size):
    line = input().split()
    matrix.append(line)
    for j in range(size):
        if matrix[i][j] == "Q":
            queens.append((i, j))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top left": (-1, -1),
    "top right": (-1, 1),
    "bottom left": (1, -1),
    "bottom right": (1, 1)
}

threats = []

for queen in queens:
    row, col = queen

    for direction in directions:
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        while next_row in range(size) and next_col in range(size):
            if matrix[next_row][next_col] == "Q":
                break
            elif matrix[next_row][next_col] == "K":
                threats.append([row, col])
            next_row += directions[direction][0]
            next_col += directions[direction][1]

if threats:
    [print(line) for line in threats]
else:
    print("The king is safe!")
