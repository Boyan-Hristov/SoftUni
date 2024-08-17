# numbers = [int(number) for number in input().split()]
#
# while True:
#     command = input().split()
#     action = command[0]
#     if action == "Finish":
#         break
#     elif action == "Add":
#         value_to_add = int(command[1])
#         numbers.append(value_to_add)
#     elif action == "Remove":
#         value_to_remove = int(command[1])
#         if value_to_remove in numbers:
#             numbers.remove(value_to_remove)
#     elif action == "Replace":
#         value_to_replace = int(command[1])
#         replacement_value = int(command[2])
#         if value_to_replace in numbers:
#             value_to_replace_index = numbers.index(value_to_replace)
#             numbers[value_to_replace_index] = replacement_value
#     elif action == "Collapse":
#         value_to_compare = int(command[1])
#         numbers = [number for number in numbers if number >= value_to_compare]
#
# print(*numbers, sep=" ")


def add(value_to_add: int, sequence: list) -> list:
    sequence.append(value_to_add)
    return sequence


def remove(value_to_remove: int, sequence: list) -> list:
    if value_to_remove in sequence:
        sequence.remove(value_to_remove)
    return sequence


def replace(value_to_replace: int, replacement_value: int, sequence: list) -> list:
    if value_to_replace in sequence:
        value_to_replace_index = sequence.index(value_to_replace)
        sequence[value_to_replace_index] = replacement_value
    return sequence


def collapse(value_to_compare: int, sequence: list) -> list:
    sequence = [number for number in sequence if number >= value_to_compare]
    return sequence


numbers = [int(number) for number in input().split()]

while True:
    command = input().split()
    action = command[0]
    if action == "Finish":
        break
    elif action == "Add":
        numbers = add(int(command[1]), numbers)
    elif action == "Remove":
        numbers = remove(int(command[1]), numbers)
    elif action == "Replace":
        numbers = replace(int(command[1]), int(command[2]), numbers)
    elif action == "Collapse":
        numbers = collapse(int(command[1]), numbers)

print(*numbers, sep=" ")
