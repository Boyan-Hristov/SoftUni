presents = int(input())
size = int(input())

matrix = []
nice_kids = 0
nice_kids_visited = 0
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
        if matrix[i][j] == "S":
            row, column = i, j
        elif matrix[i][j] == "V":
            nice_kids += 1

command = input()
while not command == "Christmas morning":
    matrix[row][column] = "-"
    row += directions[command][0]
    column += directions[command][1]

    if row in range(size) and column in range(size):

        if matrix[row][column] == "V":
            nice_kids_visited += 1
            presents -= 1
            matrix[row][column] = "-"

        elif matrix[row][column] == "C":
            for coordinates in directions.values():
                row += coordinates[0]
                column += coordinates[1]

                if matrix[row][column].isalpha():
                    if matrix[row][column] == "V":
                        nice_kids_visited += 1

                    presents -= 1
                    matrix[row][column] = "-"

                row -= coordinates[0]
                column -= coordinates[1]

    matrix[row][column] = "S"
    if presents <= 0 or nice_kids_visited == nice_kids:
        # print("Santa ran out of presents!")
        break
    command = input()

if not presents and nice_kids_visited < nice_kids:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids_visited == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_visited} nice kid/s.")
