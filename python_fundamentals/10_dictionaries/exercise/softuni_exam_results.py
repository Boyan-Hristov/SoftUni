command = input()
students = {}
submissions = {}
while command != "exam finished":
    command_info = command.split("-")
    if len(command_info) == 3:
        username = command_info[0]
        language = command_info[1]
        points = int(command_info[2])
        if username not in students.keys():
            students[username] = {}
        if language not in students[username]:
            students[username][language] = points
        else:
            if points > students[username][language]:
                students[username][language] = points
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
    elif len(command_info) == 2:
        user = command_info[0]
        if user in students.keys():
            students.pop(user)

    command = input()

print("Results:")
for student, results in students.items():
    for value in results.values():
        print(f"{student} | {value}")
print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
