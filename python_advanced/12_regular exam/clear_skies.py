size = int(input())

matrix = []
position = []

enemies = 4
armor = 300

for i in range(size):
    line = list(input())
    matrix.append(line)
    if "J" in line:
        position = [i, line.index("J")]
        matrix[i][line.index("J")] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = position

while enemies > 0:
    command = input()
    row += directions[command][0]
    col += directions[command][1]

    if matrix[row][col] == "R":
        armor = min(300, armor + 100)
        matrix[row][col] = "-"

    elif matrix[row][col] == "E":
        matrix[row][col] = "-"
        enemies -= 1
        if enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
                break

matrix[row][col] = "J"

[print(*line, sep="") for line in matrix]
