number_of_rows = int(input())
field = []

for i in range(number_of_rows):
    row = [int(number) for number in input().split()]
    field.append(row)
attacked_squares = [s for s in input().split()]

destroyed_ships = 0
for square in attacked_squares:
    attacked_position = square.split("-")
    attacked_row = int(attacked_position[0])
    attacked_column = int(attacked_position[1])
    attacked_square = field[attacked_row][attacked_column]
    attacked_square -= 1
    field[attacked_row][attacked_column] = attacked_square
    if attacked_square == 0:
        destroyed_ships += 1

print(destroyed_ships)
