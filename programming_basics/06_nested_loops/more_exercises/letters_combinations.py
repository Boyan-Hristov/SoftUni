interval_start = input()
interval_finish = input()
wild_letter = input()

combinations_count = 0

start = ord(interval_start)
finish = ord(interval_finish)
letter_combinations = ""

for first_letter in range(start, finish + 1):
    if not chr(first_letter) == wild_letter:
        for second_letter in range(start, finish + 1):
            if not chr(second_letter) == wild_letter:
                for third_letter in range(start, finish + 1):
                    if not chr(third_letter) == wild_letter:
                        combinations_count += 1
                        letter_combinations += chr(first_letter) + chr(second_letter) + chr(third_letter) + " "
print(f"{letter_combinations}{combinations_count}")