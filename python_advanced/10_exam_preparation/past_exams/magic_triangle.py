def get_magic_triangle(number: int) -> list:
    matrix = []
    for i in range(number):
        matrix.append([])
        for j in range(i + 1):
            matrix[i].append(1)

    for i in range(1, len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) + 1):
            if j - 1 not in range(len(row)):
                matrix[i + 1][j] = matrix[i][0]
            else:
                if j == len(row):
                    matrix[i + 1][j] = matrix[i][len(row) - 1]
                else:
                    matrix[i + 1][j] = matrix[i][j - 1] + matrix[i][j]

    return matrix


print(get_magic_triangle(5))
