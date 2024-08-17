def hidden_message(message: list) -> str:
    numbers = [number for number in initial_message if number.isdigit()]
    non_numbers = [character for character in initial_message if not character.isdigit()]
    take_list = []
    skip_list = []
    for index in range(len(numbers)):
        if index % 2 == 0:
            take_list.append(int(numbers[index]))
        else:
            skip_list.append(int(numbers[index]))
    result_string = ""
    for (take, skip) in zip(take_list, skip_list):
        taken_string = non_numbers[:take]
        result_string += "".join(taken_string)
        non_numbers = non_numbers[take:]
        non_numbers = non_numbers[skip:]
    return result_string


initial_message = list(input())
print(hidden_message(initial_message))
