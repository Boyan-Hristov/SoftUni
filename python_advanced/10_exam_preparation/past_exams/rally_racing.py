size = int(input())
race_car = input()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
position = [0, 0]
kilometers_passed = 0
tunnels = []

for i in range(size):
    line = input().split()
    matrix.append(line)
    for j in range(size):
        if line[j] == "T":
            tunnels.append([i, j])

row, column = position

command = input()
while not command == "End":
    row += directions[command][0]
    column += directions[command][1]
    kilometers_passed += 10

    if matrix[row][column] == "T":
        kilometers_passed += 20
        tunnels.remove([row, column])
        matrix[row][column] = "."
        row, column = tunnels[0]
        matrix[row][column] = "."

    elif matrix[row][column] == "F":
        matrix[row][column] = "C"
        print(f"Racing car {race_car} finished the stage!")
        break

    command = input()

else:
    matrix[row][column] = "C"
    print(f"Racing car {race_car} DNF.")

print(f"Distance covered {kilometers_passed} km.")
[print(*row, sep="") for row in matrix]
