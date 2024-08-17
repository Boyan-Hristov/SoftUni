from collections import deque


def get_players_and_symbols():
    player_one_name = input("First player name: ")
    player_two_name = input("Second player name: ")
    print()

    while True:
        player_one_sign = input(f"{player_one_name.capitalize()}, would you like to play with 'X' or 'O'?: ").upper()
        print()
        if player_one_sign in ("X", "O"):
            break
        else:
            print("Invalid symbol, please try again.")
    player_two_sign = "X" if player_one_sign == "O" else "O"

    players.append((player_one_name, player_one_sign))
    players.append((player_two_name, player_two_sign))

    print("This is the numeration of the board:")
    print_board()

    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = " "


def print_board():
    [print(f"|  {'  |  '.join(row)}  |") for row in board]


def mark_position():
    global turns

    while True:
        try:
            position = int(input(f"{player_name.capitalize()}, choose a free position [1-9]: "))
        except ValueError:
            print("Invalid position, please try again.")
            print()
        else:
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
            if row in range(SIZE) and col in range(SIZE) and board[row][col] == " ":
                turns += 1
                board[row][col] = player_sign
                print_board()
                break
            else:
                print("Invalid position, please try again.")


def check_winner(symbol):
    rows_win = any([all([el == symbol for el in row]) for row in board])
    cols_win = any([all([board[j][i] == symbol for j in range(SIZE)]) for i in range(SIZE)])

    main_diagonal_win = all([board[i][i] == symbol for i in range(SIZE)])
    secondary_diagonal_win = all([board[i][SIZE - i - 1] == symbol for i in range(SIZE)])

    if any((rows_win, cols_win, main_diagonal_win, secondary_diagonal_win)):
        print(f"{player_name.capitalize()} wins!")
        exit()


SIZE = 3
turns = 0

board = [[str(i + j) for j in range(SIZE)] for i in range(1, SIZE * SIZE, SIZE)]
players = deque()

get_players_and_symbols()
print(f"{players[0][0].capitalize()} starts first!")

while True:
    player_name, player_sign = players[0]
    mark_position()
    check_winner(player_sign)
    if turns == 9:
        print("Draw!")
        break
    players.rotate()

# TO DO: create a text file to store data about each game
