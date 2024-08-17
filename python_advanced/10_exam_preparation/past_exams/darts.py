from math import ceil

size = 7
players = input().split(", ")

matrix = []

for i in range(size):
    matrix.append(input().split())

scores = {
    players[0]: 501,
    players[1]: 501
}

counter = 0

while scores[players[0]] > 0 and scores[players[1]] > 0:
    counter += 1
    coordinates = input().split(", ")
    row = int(coordinates[0].lstrip("("))
    col = int(coordinates[1].rstrip(")"))

    if row in range(size) and col in range(size):

        if matrix[row][col] == "B":
            # score_1 = 0 if not counter % 2 == 0 else score_2 = 0
            result = 501
        elif matrix[row][col] == "D":
            result = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
        elif matrix[row][col] == "T":
            result = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
        else:
            result = int(matrix[row][col])

        if not counter % 2 == 0:
            scores[players[0]] -= result
        else:
            scores[players[1]] -= result

if scores[players[0]] < scores[players[1]]:
    winner = players[0]
else:
    winner = players[1]

print(f"{winner} won the game with {ceil(counter / 2)} throws!")
