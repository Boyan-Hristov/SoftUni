size = int(input())
matrix = [list(input()) for i in range(size)]

moves = (
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2)
)

knights = {}

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "K":
            knight_position = (i, j)
            attacks = 0

            for move in moves:
                row, column = i + move[0], j + move[1]
                if row in range(size) and column in range(size):
                    if matrix[row][column] == "K":
                        attacks += 1
            if attacks > 0:
                knights[knight_position] = attacks

# knights = dict(sorted(knights.items(), key=lambda x: -x[1]))
knights = dict(sorted(knights.items(), key=lambda z: (-z[1], z[0][0])))

if knights:
    knights_removed = 0
    for position in knights.keys():
        r, c = position[0], position[1]
        for move in moves:
            x, y = r + move[0], c + move[1]
            if x in range(size) and y in range(size):
                if matrix[x][y] == "K":
                    matrix[r][c] = 0
                    knights_removed += 1
                    break
    print(knights_removed)

else:
    print(0)
