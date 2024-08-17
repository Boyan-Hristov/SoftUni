size = int(input())

board = []
starting_position = []
money = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(size):
    row = list(input())
    board.append(row)
    if "G" in row:
        starting_position = [i, row.index("G")]

row, column = starting_position[0], starting_position[1]

command = input()

while not command == "end":
    board[row][column] = "-"
    row += directions[command][0]
    column += directions[command][1]

    if row not in range(size) or column not in range(size):
        money = 0
        print("Game over! You lost everything!")
        break

    if board[row][column] == "W":
        money += 100

    elif board[row][column] == "P":
        money -= 200

    elif board[row][column] == "J":
        money += 100_000
        board[row][column] = "G"
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        [print(*row, sep="") for row in board]

    if money <= 0:
        print("Game over! You lost everything!")
        break

    command = input()

board[row][column] = "G"

if 0 < money < 100_000:
    print(f"End of the game. Total amount: {money}$")
    [print(*row, sep="") for row in board]

