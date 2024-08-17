number_of_rows = int(input())
board = []
for i in range(number_of_rows):
    row = input().split()
    board.append(row)
max_connected_dots = 1
connected_dots = max_connected_dots
horizontal_connection = True
vertical_connection = True
for row_index in range(len(board)):
    for index in range(len(board[row_index])):
        if board[row_index][index] == ".":
            if index + 1 <= len(board[row_index]) - 1:
                if board[row_index][index + 1] == ".":
                    connected_dots += 1
                else:
                    horizontal_connection = False
            if row_index + 1 <= len(board) - 1:
                if board[row_index + 1][index] == ".":
                    connected_dots += 1
                else:
                    vertical_connection = False
            if horizontal_connection == False and vertical_connection == False:
                if connected_dots > max_connected_dots:
                    max_connected_dots = connected_dots
                    connected_dots = 1

print(max_connected_dots)
