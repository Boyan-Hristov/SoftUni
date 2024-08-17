number_of_students = int(input())
students = {}

for i in range(number_of_students):
    name, grade = input().split()
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = [f"{grade:.2f}" for grade in grades]
    print(f"{student} -> {' '.join(formatted_grades)} (avg: {average_grade:.2f})")
