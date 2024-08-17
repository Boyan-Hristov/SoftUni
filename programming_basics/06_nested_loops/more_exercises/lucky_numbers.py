n = int(input())

lucky_numbers = ""

for first_number in range(1, 10):
    for second_number in range(1, 10):
        for third_number in range(1, 10):
            for fourth_number in range(1, 10):
                if first_number + second_number == third_number + fourth_number \
                        and n % (first_number + second_number) == 0:
                    lucky_numbers += str(first_number) + str(second_number) + str(third_number) + \
                                     str(fourth_number) + " "
print(lucky_numbers)
