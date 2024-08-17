rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for i in range(rows)]

identical_squares = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        element = matrix[i][j]
        right_element = matrix[i][j + 1]
        bottom_element = matrix[i + 1][j]
        diagonal_element = matrix[i + 1][j + 1]

        if element == right_element == bottom_element == diagonal_element:
            identical_squares += 1

print(identical_squares)
