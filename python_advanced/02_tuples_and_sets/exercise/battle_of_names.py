number_of_lines = int(input())

odd_numbers = set()
even_numbers = set()

for i in range(1, number_of_lines + 1):
    name = input()
    name_value = 0
    for char in name:
        name_value += ord(char)
    name_value //= i
    if name_value % 2 == 0:
        even_numbers.add(name_value)
    else:
        odd_numbers.add(name_value)

odd_numbers_sum = sum(odd_numbers)
even_numbers_sum = sum(even_numbers)

if odd_numbers_sum == even_numbers_sum:
    sets_union = odd_numbers.union(even_numbers)
    print(*sets_union, sep=", ")
elif odd_numbers_sum > even_numbers_sum:
    different_values = odd_numbers.difference(even_numbers)
    print(*different_values, sep=", ")
else:
    different_symmetric_values = odd_numbers.symmetric_difference(even_numbers)
    print(*different_symmetric_values, sep=", ")
