factor = int(input())
numbers_count = int(input())

my_list = []
current_number = factor

while len(my_list) < numbers_count:
    if current_number % factor == 0 and current_number > 0:
        my_list.append(current_number)
    current_number += 1

print(my_list)

# factor = int(input())
# count = int(input())
# list_with_numbers = []
# for multiplier in range(1, count +1):
#     list_with_numbers.append(multiplier * factor)
# print(list_with_numbers)
