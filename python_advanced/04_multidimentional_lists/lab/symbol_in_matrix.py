rows = int(input())

matrix = [list(input()) for i in range(rows)]

symbol = input()

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == symbol:
            position = (i, j)
            print(position)
            exit()
else:
    print(f"{symbol} does not occur in the matrix")
