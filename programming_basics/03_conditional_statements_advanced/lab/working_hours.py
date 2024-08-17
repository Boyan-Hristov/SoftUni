hour = int(input())
day_of_the_week = input()

status = ""
if day_of_the_week == "Monday":
    if 10 <= hour <= 18:
        status = "open"
    else:
        status = "closed"
elif day_of_the_week == "Tuesday":
    if 10 <= hour <= 18:
        status = "open"
    else:
        status = "closed"
elif day_of_the_week == "Wednesday":
    if 10 <= hour <= 18:
        status = "open"
    else:
        status = "closed"
elif day_of_the_week == "Thursday":
    if 10 <= hour <= 18:
        status = "open"
    else:
        status = "closed"
elif day_of_the_week == "Friday":
    if 10 <= hour <= 18:
        status = "open"
    else:
        status = "closed"
elif day_of_the_week == "Saturday":
    if 10 <= hour <= 18:
        status = "open"
    else:
        status = "closed"
elif day_of_the_week == "Sunday":
    status = "closed"

print(status)
