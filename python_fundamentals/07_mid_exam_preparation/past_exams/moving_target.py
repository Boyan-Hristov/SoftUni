targets = [int(number) for number in input().split()]

while True:
    command = input().split()
    action = command[0]
    if action == "End":
        break
    elif action == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if 0 <= index < len(targets) and \
                0 <= (index - radius) < len(targets) and \
                0 <= (index + radius + 1) < len(targets):
            # targets_to_remove = []
            # for target_index in range(index - radius, index + radius + 1):
            #     targets_to_remove.append(targets[target_index])
            # targets = [target for target in targets if target not in targets_to_remove]
            del targets[index - radius:index + radius + 1]
        else:
            print("Strike missed!")

print(*targets, sep="|")




