from collections import deque

ducks = {
    "Darth Vader Ducky": range(0, 61),
    "Thor Ducky": range(61, 121),
    "Big Blue Rubber Ducky": range(121, 181),
    "Small Yellow Rubber Ducky": range(181, 241)
}

ducks_given = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

time_needed = deque([int(x) for x in input().split()])
tasks = [int(y) for y in input().split()]

while time_needed and tasks:
    time = time_needed.popleft()
    task = tasks.pop()
    result = time * task

    for key, value in ducks.items():
        if result in value:
            ducks_given[key] += 1
            break
        elif result > 240:
            task -= 2
            tasks.append(task)
            time_needed.append(time)
            break

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in ducks_given.items():
    print(f"{duck}: {count}")
