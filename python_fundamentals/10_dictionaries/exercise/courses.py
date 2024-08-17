command = input()
courses = {}
while command != "end":
    course, student = command.split(" : ")
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)
    command = input()
for key, value in courses.items():
    print(f"{key}: {len(courses[key])}")
    for element in value:
        print(f"-- {element}")
