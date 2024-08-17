numbers = [int(x) for x in input().split()]
target_number = int(input())

used_numbers = set()

for number in numbers:
    result = target_number - number
    if result in numbers and number not in used_numbers and result not in used_numbers:
        print(f"{number} + {result} = {target_number}")
        used_numbers.add(number)
        used_numbers.add(result)

