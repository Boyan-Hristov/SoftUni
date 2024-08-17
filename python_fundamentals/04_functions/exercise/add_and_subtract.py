first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(n1, n2):
    result = n1 + n2
    return result


def subtract(n3, n4):
    result = n3 - n4
    return result


def add_and_subtract(n5, n6, n7):
    numbers_sum = sum_numbers(n5, n6)
    subtracted_numbers = subtract(numbers_sum, n7)
    return subtracted_numbers


print(add_and_subtract(first_number, second_number, third_number))


