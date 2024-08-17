number_of_lines = int(input())

numbers_list = []

for i in range(number_of_lines):
    number = int(input())
    numbers_list.append(number)

command = input()

filtered_list = []

if command == "even":
    for j in numbers_list:
        if j % 2 == 0:
            filtered_list.append(j)
elif command == "odd":
    for j in numbers_list:
        if j % 2 != 0:
            filtered_list.append(j)
elif command == "positive":
    for j in numbers_list:
        if j >= 0:
            filtered_list.append(j)
elif command == "negative":
    for j in numbers_list:
        if j < 0:
            filtered_list.append(j)

print(filtered_list)
