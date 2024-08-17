from math import ceil


class PositionTakenError(Exception):
    pass


def get_player_and_symbol(moves: int, players: list) -> tuple:
    if not moves % 2 == 0:
        return players[0]
    return players[1]


def is_winner(current_player, matrix):
    pass


SYMBOLS = ["X", "O"]
ROWS = 3
COLS = 3

board = []

[board.append([" ", " ", " "]) for row in range(COLS)]

player_one = input("Player one name: ")
player_two = input("Player two name: ")

player_one_symbol = input(f"{player_one} would you like to play with 'X' or 'O'? ")

while True:
    try:
        SYMBOLS.remove(player_one_symbol.upper())
    except ValueError:
        player_one_symbol = input("Invalid symbol, please choose again 'X' or 'O': ")
    else:
        player_two_symbol = SYMBOLS[0]
        player_symbols = [(player_one, player_one_symbol.upper()), (player_two, player_two_symbol)]
        break

print("This is the numeration of the board:")
print("|  1  |  2  |  3  |")
print("|  4  |  5  |  6  |")
print("|  7  |  8  |  9  |")


turns = 1

while turns <= 9:
    player, symbol = get_player_and_symbol(turns, player_symbols)
    try:
        position = int(input(f"{player}, choose a free position [1-9]: "))
        row = ceil(position / 3) - 1
        col = position % 3 - 1

        if board[row][col] == " ":
            board[row][col] = symbol
        else:
            raise PositionTakenError

    except (ValueError, IndexError, PositionTakenError):
        print("Invalid position!")
        continue

    [print(f"|  {'  |  '.join(row)}  |") for row in board]

    turns += 1
