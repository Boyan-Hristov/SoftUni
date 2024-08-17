from collections import deque

liters_available = int(input())
name = input()
queue = deque()

while not name == "Start":
    queue.append(name)
    name = input()

command = input()

while not command == "End":
    tokens = command.split()
    if tokens[0].isdigit():
        liters_requested = int(tokens[0])
        person = queue.popleft()
        if liters_available >= liters_requested:
            liters_available -= liters_requested
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    else:
        liters_refilled = int(tokens[1])
        liters_available += liters_refilled
    command = input()

print(f"{liters_available} liters left")
