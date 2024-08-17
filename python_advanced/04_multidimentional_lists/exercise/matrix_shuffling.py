# rows, columns = [int(x) for x in input().split()]
#
# matrix = [[x for x in input().split()] for i in range(rows)]
#
# command = input()
# while not command == "END":
#     tokens = command.split()
#     is_valid = True
#     if tokens[0] == "swap" and len(tokens) == 5:
#         for token in range(1, len(tokens)):
#             if tokens[token].isdigit():
#                 if int(tokens[token]) < 0 or int(tokens[token]) >= columns:
#                     is_valid = False
#             else:
#                 is_valid = False
#     else:
#         is_valid = False
#     if is_valid:
#         matrix[int(tokens[1])][int(tokens[2])], matrix[int(tokens[3])][int(tokens[4])] \
#             = matrix[int(tokens[3])][int(tokens[4])], matrix[int(tokens[1])][int(tokens[2])]
#         for row in matrix:
#             print(*row)
#     else:
#         print("Invalid input!")
#     command = input()

def validate_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_columns)


def swap_elements(some_command, indices):
    if len(indices) == 4 and validate_indices(indices) and some_command == "swap":
        row1, column1, row2, column2 = indices
        matrix[row1][column1], matrix[row2][column2] = matrix[row2][column2], matrix[row1][column1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for i in range(rows)]

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_elements(command, coordinates)
