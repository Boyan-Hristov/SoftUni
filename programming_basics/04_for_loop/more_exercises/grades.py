students_count = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
failed = 0
grade_total = 0

for student in range(students_count):
    grade = float(input())
    grade_total += grade
    if 5.00 <= grade:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_5 += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_4 += 1
    elif 2.00 <= grade <= 2.99:
        failed += 1

top_students_percent = top_students / students_count * 100
between_4_and_5_percent = between_4_and_5 / students_count * 100
between_3_and_4_percent = between_3_and_4 / students_count * 100
failed_percent = failed / students_count * 100
average_grade = grade_total / students_count

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4_percent:.2f}%")
print(f"Fail: {failed_percent:.2f}%")
print(f"Average: {average_grade:.2f}")


