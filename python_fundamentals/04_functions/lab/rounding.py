numbers = list(map(float, input().split()))


def round_number(number):
    rounded_number = round(number)
    return rounded_number


rounded_numbers = []
for current_number in numbers:
    rounded_numbers.append(round_number(current_number))

print(rounded_numbers)
