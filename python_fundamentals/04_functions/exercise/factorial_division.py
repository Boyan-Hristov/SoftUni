first_integer = int(input())
second_integer = int(input())


def factorial_division(first_number, second_number):
    first_factorial = 1
    for number in range(1, first_number + 1):
        first_factorial *= number
    second_factorial = 1
    for number in range(1, second_number + 1):
        second_factorial *= number
    result = first_factorial / second_factorial
    return f"{result:.2f}"


print(factorial_division(first_integer, second_integer))


# 02
# def calculate_the_factorial(number):
#     for current_number in range (1, number):
#         number *= current_number
#     return number     # initial number factorial -> number!
#
#
# first_number = int(input())
# second_number = int(input())
# first_number_factorial = calculate_the_factorial(first_number)
# second_number_factorial = calculate_the_factorial(second_number)
# result = first_number_factorial / second_number_factorial
# print(f"{result:.2f}")
