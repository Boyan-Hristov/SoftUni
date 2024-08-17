from sys import maxsize

size = 6

matrix = []
points = 0

prizes = {
    "Football": range(100, 200),
    "Teddy Bear": range(200, 300),
    "Lego Construction Set": range(300, maxsize)

}

for i in range(size):
    line = input().split()
    matrix.append(line)

for j in range(3):
    data = input().split(", ")
    row, col = data
    row = row.lstrip("(")
    col = col.rstrip(")")
    row = int(row)
    col = int(col)

    if row in range(size) and col in range(size):
        if matrix[row][col] == "B":
            matrix[row][col] = 0
            for k in range(6):
                if not matrix[k][col] == "B":
                    points += int(matrix[k][col])

if points >= 100:
    prize = ""
    for key, value in prizes.items():
        if points in value:
            prize = key
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
