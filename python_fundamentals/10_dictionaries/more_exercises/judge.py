contests = {}
individual_statistics = {}
while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    if contest not in contests.keys():
        contests[contest] = {}
    if username in contests[contest].keys():
        if int(points) > contests[contest][username]:
            difference = int(points) - contests[contest][username]
            contests[contest][username] = int(points)
            individual_statistics[username] += difference
    else:
        contests[contest][username] = int(points)
        if username not in individual_statistics.keys():
            individual_statistics[username] = 0
        individual_statistics[username] += int(points)


for course, results in contests.items():
    results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
    # results = dict(sorted(results.items(), key=lambda x: x[0]))
    # results = dict(sorted(results.items(), key=lambda x: -x[1]))
    print(f"{course}: {len(results)} participants")
    index = 1
    for student, points in results.items():
        print(f"{index}. {student} <::> {points}")
        index += 1
individual_statistics = dict(sorted(individual_statistics.items(), key=lambda x: (-x[1], x[0])))
# individual_statistics = dict(sorted(individual_statistics.items(), key=lambda x: x[0]))
# individual_statistics = dict(sorted(individual_statistics.items(), key=lambda x: -x[1]))
print("Individual standings:")
individual_index = 1
for user, record in individual_statistics.items():
    print(f"{individual_index}. {user} -> {record}")
    individual_index += 1
