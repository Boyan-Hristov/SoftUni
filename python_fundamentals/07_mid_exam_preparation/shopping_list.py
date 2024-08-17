def urgent(some_item: str) -> list:
    if some_item not in shopping_list:
        shopping_list.insert(0, some_item)
    return shopping_list


def unnecessary(some_item: str) -> list:
    if some_item in shopping_list:
        shopping_list.remove(some_item)
    return shopping_list


def correct(first_item, second_item: str) -> list:
    if first_item in shopping_list:
        index = shopping_list.index(first_item)
        shopping_list[index] = second_item
    return shopping_list


def rearrange(some_item: str) -> list:
    if some_item in shopping_list:
        shopping_list.remove(some_item)
        shopping_list.append(some_item)
    return shopping_list


shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command_info = command.split()
    action = command_info[0]
    if action == "Urgent":
        item = command_info[1]
        urgent(item)
    elif action == "Unnecessary":
        item = command_info[1]
        unnecessary(item)
    elif action == "Correct":
        old_item = command_info[1]
        new_item = command_info[2]
        correct(old_item, new_item)
    elif action == "Rearrange":
        item = command_info[1]
        rearrange(item)

print(", ".join(shopping_list))
