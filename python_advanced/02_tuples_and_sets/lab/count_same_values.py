numbers = tuple([float(x) for x in input().split()])
unique_numbers = {}

for number in numbers:
    if number not in unique_numbers:
        unique_numbers[number] = numbers.count(number)

for num, count in unique_numbers.items():
    print(f"{num} - {count} times")
