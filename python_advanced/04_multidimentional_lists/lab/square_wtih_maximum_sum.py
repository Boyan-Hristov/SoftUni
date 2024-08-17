rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

submatrix = []
biggest_sum = float("-inf")
for i in range(rows - 1):
    for j in range(columns - 1):
        current_element = matrix[i][j]
        right_element = matrix[i][j + 1]
        bottom_element = matrix[i + 1][j]
        diagonal_element = matrix[i + 1][j + 1]
        if current_element + right_element + bottom_element + diagonal_element > biggest_sum:
            biggest_sum = current_element + right_element + bottom_element + diagonal_element
            submatrix = [[current_element, right_element], [bottom_element, diagonal_element]]

for row in submatrix:
    print(*row)
print(biggest_sum)
