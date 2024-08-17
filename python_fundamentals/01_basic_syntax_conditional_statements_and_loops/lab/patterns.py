number = int(input())
for row in range(number + 1):
    for column in range(1):
        print(row * "*")
for bottom_row in range(number - 1, - 1, -1):
    for column in range(1):
        print(bottom_row * "*")
