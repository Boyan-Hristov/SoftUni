size = 8

matrix = []
white_position = []
black_position = []

white_diagonals = (
    (-1, -1),
    (-1, 1)
)

black_diagonals = (
    (1, -1),
    (1, 1)
)

rows = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}

cols = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for i in range(size):
    line = input().split()
    matrix.append(line)
    if "w" in line:
        white_position = [i, line.index("w")]
    elif "b" in line:
        black_position = [i, line.index("b")]

counter = 0

white_row, white_col = white_position
black_row, black_col = black_position


while True:
    counter += 1
    if not counter % 2 == 0:
        for diagonal in white_diagonals:
            row = white_row + diagonal[0]
            col = white_col + diagonal[1]
            if matrix[row][col] == "b":
                print(f"Game over! White win, capture on {cols[col] + rows[row]}.")
                exit()
        else:
            matrix[white_row][white_col] = "-"
            white_row += -1
            if white_row == 0:
                print(f"Game over! White pawn is promoted to a queen at {cols[white_col] + rows[white_row]}.")
                exit()
            matrix[white_row][white_col] = "w"

    else:
        for diagonal in black_diagonals:
            row = black_row + diagonal[0]
            col = black_col + diagonal[1]
            if matrix[row][col] == "b":
                print(f"Game over! Black win, capture on {cols[col] + rows[row]}.")
                exit()
        else:
            matrix[black_row][black_col] = "-"
            black_row += 1
            if black_row == 7:
                print(f"Game over! Black pawn is promoted to a queen at {cols[black_col] + rows[black_row]}.")
                exit()
            matrix[black_row][black_col] = "b"
