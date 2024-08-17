# rows = int(input())
#
# matrix = []
#
# for i in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# data = input().split()
#
# for coordinates in data:
#     tokens = coordinates.split(",")
#     row, column = int(tokens[0]), int(tokens[1])
#
#     damage = matrix[row][column]
#     matrix[row][column] = 0
#
#     if row - 1 in range(rows):
#         if matrix[row - 1][column] > 0:
#             matrix[row - 1][column] -= damage
#         if column - 1 in range(rows):
#             if matrix[row - 1][column - 1] > 0:
#                 matrix[row - 1][column - 1] -= damage
#         if column + 1 in range(rows):
#             if matrix[row - 1][column + 1] > 0:
#                 matrix[row - 1][column + 1] -= damage
#
#     if row + 1 in range(rows):
#         if matrix[row + 1][column] > 0:
#             matrix[row + 1][column] -= damage
#         if column - 1 in range(rows):
#             if matrix[row + 1][column - 1] > 0:
#                 matrix[row + 1][column - 1] -= damage
#         if column + 1 in range(rows):
#             if matrix[row + 1][column + 1] > 0:
#                 matrix[row + 1][column + 1] -= damage
#
#     if column - 1 in range(rows):
#         if matrix[row][column - 1] > 0:
#             matrix[row][column - 1] -= damage
#     if column + 1 in range(rows):
#         if matrix[row][column + 1] > 0:
#             matrix[row][column + 1] -= damage
#
# alive_cells = [[x for x in line if x > 0] for line in matrix]
# flattened = [x for row in alive_cells for x in row]
#
# print(f"Alive cells: {len(flattened)}")
# print(f"Sum: {sum(flattened)}")
#
# for row in matrix:
#     print(*row)

rows = int(input())

matrix = [[int(x) for x in input().split()] for i in range(rows)]
coordinates = ((int(x) for x in c.split(",")) for c in input().split())

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1),
    (0, 0)
)

for row, column in coordinates:
    if matrix[row][column] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, column + y

        if 0 <= r < rows and 0 <= c < rows:
            matrix[r][c] -= matrix[row][column] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(rows) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]
