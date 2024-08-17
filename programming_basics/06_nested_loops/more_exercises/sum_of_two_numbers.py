interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

counter = 0
magic_counter = 0

for first_number in range(interval_start, interval_end + 1):
    if not magic_counter == 0:
        break
    for second_number in range(interval_start, interval_end + 1):
        counter += 1
        if first_number + second_number == magic_number:
            print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
            magic_counter += 1
            break
if magic_counter == 0:
    print(f"{counter} combinations - neither equals {magic_number}")


