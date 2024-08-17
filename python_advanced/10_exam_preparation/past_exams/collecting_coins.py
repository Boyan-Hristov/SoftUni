size = int(input())

matrix = []
position = []
path = []
coins = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

valid_commands = (
    "up",
    "down",
    "left",
    "right"
)

for i in range(size):
    line = input().split()
    matrix.append(line)
    if "P" in line:
        position = [i, line.index("P")]
        matrix[i][line.index("P")] = 0

path.append(position)
row, col = position

command = input()

while True:
    if command not in valid_commands:
        continue
    row += directions[command][0]
    col += directions[command][1]

    if row not in range(size):
        if command == "up":
            row = size - 1
        elif command == "down":
            row = 0
    elif col not in range(size):
        if command == "left":
            col = size - 1
        elif command == "right":
            col = 0

    path.append([row, col])

    if matrix[row][col] == "X":
        print(f"Game over! You've collected {coins // 2} coins.")
        break

    else:
        coins += int(matrix[row][col])
        matrix[row][col] = 0
        if coins >= 100:
            print(f"You won! You've collected {int(coins)} coins.")
            break

    command = input()

print("Your path:")
[print(line) for line in path]
