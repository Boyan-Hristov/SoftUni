rows, columns = [int(x) for x in input().split()]

matrix = []
position = []
total_players = 0
moves = 0
players_touched = 0

for i in range(rows):
    line = input().split()
    matrix.append(line)
    if "B" in line:
        position = [i, line.index("B")]
        matrix[i][line.index("B")] = "-"
    if "P" in line:
        total_players += line.count("P")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, column = position
command = input()

while not command == "Finish":
    row += directions[command][0]
    column += directions[command][1]

    if (row not in range(rows) or column not in range(columns)) or matrix[row][column] == "O":
        row -= directions[command][0]
        column -= directions[command][1]
    else:
        if matrix[row][column] == "P":
            players_touched += 1
        moves += 1

    if players_touched == total_players:
        break

    command = input()

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves}")
