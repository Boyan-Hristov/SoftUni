size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
position = []
cruisers = 3
hits_taken = 0

for i in range(size):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        position = [i, line.index("S")]
        matrix[i][line.index("S")] = "-"

row, column = position

command = input()
while True:
    row += directions[command][0]
    column += directions[command][1]

    if row in range(size) and column in range(size):
        if matrix[row][column] == "*":
            matrix[row][column] = "-"
            hits_taken += 1
            if hits_taken == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {column}]!")
                break

        elif matrix[row][column] == "C":
            matrix[row][column] = "-"
            cruisers -= 1
            if cruisers == 0:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break

    command = input()

matrix[row][column] = "S"

[print(*row, sep="") for row in matrix]
