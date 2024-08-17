import os

path = os.path.join("..", "resources", "numbers.txt")

file = open(path)

numbers_sum = 0

for line in file:
    numbers_sum += int(line)

print(numbers_sum)
file.close()
