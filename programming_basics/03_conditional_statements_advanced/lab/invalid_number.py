number = int(input())

status = ""
if 100 <= number <= 200 or number == 0:
    status = ""
else:
    status = "invalid"

print(status)
