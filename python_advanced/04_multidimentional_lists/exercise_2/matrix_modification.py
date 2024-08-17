def validate_coordinates(r: int, c: int) -> bool:
    if r in range(rows) and c in range(len(matrix[r])):
        return True
    else:
        return False


def add(r: int, c: int, v: int) -> list:
    matrix[r][c] += v
    return matrix


def subtract(r: int, c: int, v: int) -> list:
    matrix[r][c] -= v
    return matrix


rows = int(input())
matrix = [[int(x) for x in input().split()] for i in range(rows)]

valid_rows = range(rows)

while True:
    tokens = input().split()
    if tokens[0] == "END":
        break

    command = tokens[0]
    row, column, value = int(tokens[1]), int(tokens[2]), int(tokens[3])

    if validate_coordinates(row, column):
        if command == "Add":
            matrix = add(row, column, value)
        elif command == "Subtract":
            matrix = subtract(row, column, value)
    else:
        print("Invalid coordinates")

[print(*row) for row in matrix]
