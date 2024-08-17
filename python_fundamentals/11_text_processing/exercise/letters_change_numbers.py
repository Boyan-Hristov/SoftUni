strings = input().split()
total_sum = 0
for string in strings:
    result = 0
    number = int(string[1:-1])
    first_letter = string[0]
    second_letter = string[-1]

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        result = number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        result = number * first_letter_position

    if second_letter.isupper():
        second_letter_position = ord(second_letter) - 64
        result -= second_letter_position
    elif second_letter.islower():
        second_letter_position = ord(second_letter) - 96
        result += second_letter_position

    total_sum += result

print(f"{total_sum:.2f}")
