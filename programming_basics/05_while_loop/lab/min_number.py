import sys

command = input()
min_number = sys.maxsize

while command != "Stop":
    command_value = int(command)
    if command_value < min_number:
        min_number = command_value
    command = input()

print(min_number)