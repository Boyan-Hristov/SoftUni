start = int(input())
final = int(input())
magic_number = int(input())

combinations_count = 0
is_combination_found = False
for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        combinations_count += 1
        if first_number + second_number == magic_number:
            is_combination_found = True
            break
    if first_number + second_number == magic_number:
        break

if is_combination_found:
    print(f"Combination N:{combinations_count} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
