bad_grades_count = int(input())
bad_grades_received = 0
problems_count = 0
problem_name = ""
grades_sum = 0

is_Failed = False

command = input()

while not command == "Enough":
    grade = int(input())
    problems_count += 1
    grades_sum += grade
    if grade <= 4:
        bad_grades_received += 1
        if bad_grades_received == bad_grades_count:
            is_Failed = True
            break
    else:
        problem_name = command
    command = input()

average_grade = grades_sum / problems_count
if not is_Failed:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {problem_name}")
else:
    print(f"You need a break, {bad_grades_received} poor grades.")