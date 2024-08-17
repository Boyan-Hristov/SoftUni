def collect(items: list, some_item: str) -> list:
    if some_item not in items:
        items.append(some_item)
    return items


def drop(items: list, some_item: str) -> list:
    if some_item in items:
        items.remove(some_item)
    return items


def combine(items: list, old_item: str, new_item: str) -> list:
    if old_item in items:
        old_item_index = items.index(old_item)
        items.insert(old_item_index + 1, new_item)
    return items


def renew(items: list, some_item: str) -> list:
    if some_item in items:
        items.remove(some_item)
        items.append(some_item)
    return items


inventory = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    command_info = command.split(" - ")
    action = command_info[0]
    if action == "Collect":
        item = command_info[1]
        inventory = collect(inventory, item)
    elif action == "Drop":
        item = command_info[1]
        inventory = drop(inventory, item)
    elif action == "Combine Items":
        items_to_combine = command_info[1].split(":")
        first_item = items_to_combine[0]
        second_item = items_to_combine[1]
        inventory = combine(inventory, first_item, second_item)
    elif action == "Renew":
        item = command_info[1]
        inventory = renew(inventory, item)

print(", ".join(inventory))
