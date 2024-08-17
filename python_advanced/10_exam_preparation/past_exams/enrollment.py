def gather_credits(credits_needed: int, *args) -> str:
    result = ""
    courses = []
    credits_earned = 0

    for data in args:
        course, credit = data[0], int(data[1])
        if credits_earned < credits_needed:
            if course not in courses:
                credits_earned += credit
                courses.append(course)
        else:
            break

    if credits_earned >= credits_needed:
        result += f"Enrollment finished! Maximum credits: {credits_earned}.\n"
        result += f"Courses: {', '.join(sorted(courses))}"
    else:
        credits_shortage = credits_needed - credits_earned
        result += f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

    return result


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
