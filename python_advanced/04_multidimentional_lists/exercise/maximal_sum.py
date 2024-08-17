rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for i in range(rows)]

maximal_sum = float("-inf")
submatrix = []

for i in range(rows - 2):
    for j in range(columns - 2):
        first_row = matrix[i][j:j + 3]
        second_row = matrix[i + 1][j: j + 3]
        third_row = matrix[i + 2][j:j + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > maximal_sum:
            maximal_sum = current_sum
            submatrix = [first_row, second_row, third_row]

print(f"Sum = {maximal_sum}")
for row in submatrix:
    print(*row)
