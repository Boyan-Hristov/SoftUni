integer = int(input())
for number in range(1, integer + 1):
    is_special = False
    number_as_string = str(number)
    digits_sum = 0
    for digit in number_as_string:
        digits_sum += int(digit)
        if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
            is_special = True
    print(f"{number} -> {is_special}")
