integer_numbers = input()
number = int(input())

numbers_list = integer_numbers.split(" ")

integers_list = []

for element in numbers_list:
    integers_list.append(int(element))

for i in range(number):
    integers_list.remove(min(integers_list))

integers_list_as_string = []
for i in integers_list:
    integers_list_as_string.append(str(i))

integers_as_string = ", ".join(integers_list_as_string)
print(integers_as_string)
