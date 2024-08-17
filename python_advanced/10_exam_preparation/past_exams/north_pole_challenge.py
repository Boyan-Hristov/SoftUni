rows, columns = [int(x) for x in input().split(", ")]

matrix = []
position = []
decorations = 0
gifts = 0
cookies = 0

decorations_found = 0
gifts_found = 0
cookies_found = 0

for i in range(rows):
    line = input().split()
    matrix.append(line)
    if "Y" in line:
        position = [i, line.index("Y")]
        matrix[i][line.index("Y")] = "x"
    if "D" in line:
        decorations += line.count("D")
    if "G" in line:
        gifts += line.count("G")
    if "C" in line:
        cookies += line.count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = position

all_found = False
command = input()

while not command == "End":
    tokens = command.split("-")
    direction, steps = tokens[0], int(tokens[1])

    for j in range(steps):
        row += directions[direction][0]
        col += directions[direction][1]

        if row not in range(rows):
            if direction == "up":
                row = rows - 1
            elif direction == "down":
                row = 0

        elif col not in range(columns):
            if direction == "left":
                col = columns - 1
            elif direction == "right":
                col = 0

        if matrix[row][col] == "D":
            decorations_found += 1
        elif matrix[row][col] == "G":
            gifts_found += 1
        elif matrix[row][col] == "C":
            cookies_found += 1

        matrix[row][col] = "x"

        if sum((decorations, gifts, cookies)) == sum((decorations_found, gifts_found, cookies_found)):
            print("Merry Christmas!")
            all_found = True
            break

    if all_found:
        break

    command = input()

matrix[row][col] = "Y"

print("You've collected:")
print(f"- {decorations_found} Christmas decorations")
print(f"- {gifts_found} Gifts")
print(f"- {cookies_found} Cookies")
[print(*line) for line in matrix]
