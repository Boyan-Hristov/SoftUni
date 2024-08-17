# student_name = input()
# current_year = 1
# total_grades = 0
# failed_attempts = 0
# is_excluded = False
# while current_year < 13:
#     grade = float(input())
#     if grade >= 4.00:
#         current_year += 1
#         total_grades += grade
#     else:
#         failed_attempts += 1
#         if failed_attempts > 1:
#             print(f"{student_name} has been excluded at {current_year} grade")
#             is_excluded = True
#             break
#
#
# average_grade = total_grades / 12
# if is_excluded == False:
#     print(f"{student_name} graduated. Average grade: {average_grade:.2f}")



student_name = input()
current_year = 1
total_grades = 0
failed_attempts = 0
while current_year <= 12:
    grade = float(input())
    if grade < 4.00:
        failed_attempts += 1
        if failed_attempts > 1:
            break
        continue
    current_year += 1
    total_grades += grade

average_grade = total_grades / 12
if current_year <= 12:
    print(f"{student_name} has been excluded at {current_year} grade")
else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")