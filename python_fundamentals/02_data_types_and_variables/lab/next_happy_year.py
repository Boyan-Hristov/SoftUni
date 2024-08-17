year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    digits = ""
    for digit in year_as_string:
        digits += digit
    if len(set(digits)) == len(year_as_string):
        print(year)
        break

