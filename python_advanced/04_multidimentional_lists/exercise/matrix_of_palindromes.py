rows, columns = [int(x) for x in input().split()]

matrix = []
first_letter = ord("a")

for i in range(rows):
    row = []
    for j in range(columns):
        string = chr(first_letter + i) + chr(first_letter + i + j) + chr(first_letter + i)
        row.append(string)
    matrix.append(row)

for row in matrix:
    print(*row)
