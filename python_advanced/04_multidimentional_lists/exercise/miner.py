from collections import deque

size = int(input())
commands = deque([x for x in input().split()])

matrix = []
starting_position = []
coal = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for i in range(size):
    data = input().split()
    matrix.append(data)
    for j in range(len(data)):
        if data[j] == "s":
            starting_position.extend([i, j])
        elif data[j] == "c":
            coal += 1

row, column = starting_position[0], starting_position[1]

while commands:
    command = commands.popleft()
    row += directions[command][0]
    column += directions[command][1]
    if row in range(size) and column in range(size):
        target_position = matrix[row][column]
        if target_position == "c":
            matrix[row][column] = "*"
            coal -= 1
            if coal == 0:
                print(f"You collected all coal! ({row}, {column})")
                break
        elif target_position == "e":
            print(f"Game over! ({row}, {column})")
            break
    else:
        row -= directions[command][0]
        column -= directions[command][1]

else:
    print(f"{coal} pieces of coal left. ({row}, {column})")
