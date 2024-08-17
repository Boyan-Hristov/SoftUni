size = 6

matrix = []

players = input().split(", ")

for i in range(size):
    line = input().split()
    matrix.append(line)

player_status = {
    "Tom": "ready",
    "Jerry": "ready"
}

counter = 0

while True:
    coordinates = input()
    row, column = int(coordinates[1]), int(coordinates[4])
    counter += 1

    if not counter % 2 == 0:
        active_player = players[0]
    else:
        active_player = players[1]

    if player_status[active_player] == "rest":
        player_status[active_player] = "ready"
        continue

    if matrix[row][column] == "E":
        winner = active_player
        print(f"{active_player} found the Exit and wins the game!")
        break

    elif matrix[row][column] == "T":
        players.remove(active_player)
        winner = players[0]
        print(f"{active_player} is out of the game! The winner is {winner}.")
        break

    elif matrix[row][column] == "W":
        player_status[active_player] = "rest"
        print(f"{active_player} hits a wall and needs to rest.")
