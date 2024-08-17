students_info = input().split(":")
students = {}
while not students_info[0].islower():
    students[students_info[0]] = {}
    students[students_info[0]][students_info[1]] = students_info[2]
    students_info = input().split(":")
course_name = " ".join(students_info[0].split("_"))
for name, dictionary in students.items():
    for id, course in dictionary.items():
        if course_name == course:
            print(f"{name} - {id}")
