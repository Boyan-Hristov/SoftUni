interval_start = int(input())
interval_finish = int(input())

for first_number in range(interval_start, interval_finish + 1):
    for second_number in range(interval_start, interval_finish + 1):
        for third_number in range(interval_start, interval_finish + 1):
            for fourth_number in range(interval_start, interval_finish + 1):
                if first_number % 2 == 0 and not fourth_number % 2 == 0:
                    if first_number > fourth_number:
                        if (second_number + third_number) % 2 == 0:
                            print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
                elif not first_number % 2 == 0 and fourth_number % 2 == 0:
                    if first_number > fourth_number:
                        if (second_number + third_number) % 2 == 0:
                            print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")