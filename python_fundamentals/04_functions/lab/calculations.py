operator = input()
first_number = int(input())
second_number = int(input())


def operation(operator, num_1, num_2):
    if operator == "multiply":
        result = num_1 * num_2
        return result
    elif operator == "divide":
        result = num_1 // num_2
        return result
    elif operator == "add":
        result = num_1 + num_2
        return result
    elif operator == "subtract":
        result = num_1 - num_2
        return result


print(operation(operator, first_number, second_number))