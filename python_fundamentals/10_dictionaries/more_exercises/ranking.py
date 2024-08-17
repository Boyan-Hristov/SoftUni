contests = {}
while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests[contest] = password
candidates = {}
while True:
    new_command = input()
    if new_command == "end of submissions":
        break
    current_contest, current_password, username, points = new_command.split("=>")
    if current_contest in contests.keys():
        if current_password == contests[current_contest]:
            if username in candidates.keys():
                if current_contest in candidates[username]:
                    if int(points) > candidates[username][current_contest]:
                        candidates[username][current_contest] = int(points)
                else:
                    candidates[username][current_contest] = int(points)
            else:
                candidates[username] = {}
                candidates[username][current_contest] = int(points)

best_candidate = ""
best_score = 0
for key, value in candidates.items():
    candidate_score = 0
    for nested_key, nested_value in value.items():
        candidate_score += nested_value
    if candidate_score > best_score:
        best_score = candidate_score
        best_candidate = key
candidates = dict(sorted(candidates.items(), key=lambda x: x))
print(f"Best candidate is {best_candidate} with total {best_score} points.")
print("Ranking:")
for candidate, results in candidates.items():
    print(candidate)
    results = dict(sorted(results.items(), key=lambda x: -x[1]))
    for course, score in results.items():
        print(f"#  {course} -> {score}")


