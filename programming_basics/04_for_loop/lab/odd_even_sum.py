number_count = int(input())
sum_of_numbers_at_even = 0
sum_of_numbers_at_odd = 0
for iteration in range(number_count):
    current_number = int(input())
    if iteration % 2 == 0:
        sum_of_numbers_at_even += current_number
    else:
        sum_of_numbers_at_odd += current_number

if sum_of_numbers_at_even == sum_of_numbers_at_odd:
    print("Yes")
    print(f"Sum = {sum_of_numbers_at_odd}")
else:
    difference = abs(sum_of_numbers_at_odd - sum_of_numbers_at_even)
    print("No")
    print(f"Diff = {difference}")

