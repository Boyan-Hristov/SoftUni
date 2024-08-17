from modules_09.fibonacii_sequence.core import create_sequence, locate_number

numbers = []

command = input()

while not command == "Stop":
    number = int(command.split()[-1])
    if "Create" in command:
        numbers = create_sequence(number)
        print(*numbers)
    elif "Locate" in command:
        print(locate_number(numbers, number))

    command = input()
