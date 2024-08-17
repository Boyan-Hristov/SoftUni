first_employee_students_per_hour = int(input())
second_employee_students_per_hour = int(input())
third_employee_students_per_hour = int(input())
students = int(input())

hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    students_answered_per_hour = first_employee_students_per_hour + second_employee_students_per_hour + third_employee_students_per_hour
    students -= students_answered_per_hour

print(f"Time needed: {hours}h.")