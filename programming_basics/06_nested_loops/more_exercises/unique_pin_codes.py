first_number_max_value = int(input())
second_number_max_value = int(input())
third_number_max_value = int(input())

for first_number in range(2, first_number_max_value + 1, 2):
    for second_number in range(2, second_number_max_value + 1):
        flag = True
        for p in range(2, second_number):
            if (second_number % p) == 0:
                flag = False
                break
        if flag:
            for third_number in range(2, third_number_max_value + 1, 2):
                if not first_number == 0 and not second_number == 0 and not third_number == 0:
                    print(f"{first_number} {second_number} {third_number}")
