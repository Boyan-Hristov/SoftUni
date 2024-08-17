number = int(input())

number_as_string = str(number)
first_multiplier_as_string = number_as_string[2]
second_multiplier_as_string = number_as_string[1]
third_multiplier_as_string = number_as_string[0]

first_multiplier = int(first_multiplier_as_string)
second_multiplier = int(second_multiplier_as_string)
third_multiplier = int(third_multiplier_as_string)

for loop_one in range(1, first_multiplier + 1):
    for loop_two in range(1, second_multiplier + 1):
        for loop_three in range(1, third_multiplier + 1):
            result = loop_one * loop_two * loop_three
            print(f"{loop_one} * {loop_two} * {loop_three} = {result};")
