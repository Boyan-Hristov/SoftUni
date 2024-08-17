rounds = int(input())

result = 0
zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twenty_nine = 0
thirty_to_thirty_nine = 0
forty_to_fifty = 0
invalid_numbers = 0

for current_round in range(rounds):
    number = int(input())
    if number < 0 or number > 50:
        result /= 2
        invalid_numbers += 1
    elif 0 <= number <= 9:
        result += 0.2 * number
        zero_to_nine += 1
    elif 10 <= number <= 19:
        result += 0.3 * number
        ten_to_nineteen += 1
    elif 20 <= number <= 29:
        result += 0.4 * number
        twenty_to_twenty_nine += 1
    elif 30 <= number <= 39:
        result += 50
        thirty_to_thirty_nine += 1
    elif 40 <= number <= 50:
        result += 100
        forty_to_fifty += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {zero_to_nine / rounds * 100:.2f}%")
print(f"From 10 to 19: {ten_to_nineteen / rounds * 100:.2f}%")
print(f"From 20 to 29: {twenty_to_twenty_nine / rounds * 100:.2f}%")
print(f"From 30 to 39: {thirty_to_thirty_nine / rounds * 100:.2f}%")
print(f"From 40 to 50: {forty_to_fifty / rounds * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / rounds * 100:.2f}%")