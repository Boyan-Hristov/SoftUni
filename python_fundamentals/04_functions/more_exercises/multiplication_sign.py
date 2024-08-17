def positive_negative_zero(num_1, num_2, num_3: int) -> str:
    result = ""
    negative_numbers = 0
    if num_1 < 0:
        negative_numbers += 1
    if num_2 < 0:
        negative_numbers += 1
    if num_3 < 0:
        negative_numbers += 1
    if not negative_numbers % 2 == 0:
        result = "negative"
    elif num_1 == 0 or num_2 == 0 or num_3 == 0:
        result = "zero"
    else:
        result = "positive"
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(positive_negative_zero(first_number, second_number, third_number))
