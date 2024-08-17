numbers = list(map(int, input().split(", ")))
numbers_count = len(numbers)
group_max_value = 10
while numbers_count > 0:
    group = [number for number in numbers if number <= group_max_value]
    print(f"Group of {group_max_value}'s: {group}")
    for number in group:
        numbers.remove(number)
    group_max_value += 10
    removed_numbers = len(group)
    numbers_count -= removed_numbers
