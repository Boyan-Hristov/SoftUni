number_of_students = int(input())
students = {}
for i in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = []
    students[name].append(grade)
for key, value in students.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")

