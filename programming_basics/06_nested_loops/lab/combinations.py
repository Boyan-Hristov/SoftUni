number = int(input())
combinations = 0
for first_number in range(number + 1):
    for second_number in range(number + 1):
        for third_number in range(number + 1):
            if first_number + second_number + third_number == number:
                combinations += 1
print(combinations)
