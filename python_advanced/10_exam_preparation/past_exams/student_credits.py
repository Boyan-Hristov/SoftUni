def students_credits(*args):
    result = ""
    credits_needed = 240
    courses = {}

    for data in args:
        tokens = data.split("-")
        course, max_credits, max_points, points = tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])
        if not points == 0:
            ratio = max_points / points
            courses[course] = max_credits / ratio
        else:
            courses[course] = 0

    courses = dict(sorted(courses.items(), key=lambda x: -x[1]))

    credits_obtained = sum(courses.values())
    if credits_obtained >= credits_needed:
        result += f"Diyan gets a diploma with {credits_obtained:.1f} credits.\n"
    else:
        result += f"Diyan needs {(credits_needed - credits_obtained):.1f} credits more for a diploma.\n"

    for key, value in courses.items():
        result += f"{key} - {value:.1f}\n"
    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


