import sys

command = input()
max_number = - sys.maxsize

while command != "Stop":
    command_value = int(command)
    if command_value > max_number:
        max_number = command_value
    command = input()

print(max_number)