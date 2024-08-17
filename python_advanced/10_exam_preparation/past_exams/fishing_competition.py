size = int(input())

matrix = []
starting_position = []
catch = 0
target = 20

for i in range(size):
    row = list(input())
    matrix.append(row)
    if "S" in row:
        starting_position = [i, row.index("S")]
        matrix[i][row.index("S")] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, column = starting_position[0], starting_position[1]

command = input()

while not command == "collect the nets":
    row += directions[command][0]
    column += directions[command][1]

    if row not in range(size):
        if command == "up":
            row = size - 1
        elif command == "down":
            row = 0
    elif column not in range(size):
        if command == "left":
            column = size - 1
        elif command == "right":
            column = 0

    if matrix[row][column].isdigit():
        catch += int(matrix[row][column])
        matrix[row][column] = "-"
    elif matrix[row][column] == "W":
        catch = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{row},{column}]")
        exit()

    command = input()

matrix[row][column] = "S"

if catch >= target:
    print(f"Success! You managed to reach the quota!")
else:
    print("You didn't catch enough fish and didn't reach the quota! " 
          f"You need {target - catch} tons of fish more.")

if catch > 0:
    print(f"Amount of fish caught: {catch} tons.")

if not matrix[row][column] == "W":
    [print(*row, sep="") for row in matrix]
