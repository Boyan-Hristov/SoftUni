targets = [int(number) for number in input().split()]
targets_shot = 0

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index < len(targets):
        if targets[index] != -1:
            targets_shot += 1
            eliminated_target = targets[index]
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] > eliminated_target:
                        targets[i] -= eliminated_target
                    else:
                        targets[i] += eliminated_target
targets_as_string = [str(target) for target in targets]
print(f"Shot targets: {targets_shot} -> {' '.join(targets_as_string)}")
