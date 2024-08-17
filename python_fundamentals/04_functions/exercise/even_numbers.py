numbers = list(map(int, input().split()))


def even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(even_number, numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)


# 02
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False
#
#
# number_as_string = input().split()
# numbers_as_digits = []
# for number in number_as_string:
#     numbers_as_digits.append(int(number))
# even_numbers = []
# for element in numbers_as_digits:
#     if is_even(element):
#         even_numbers.append(element)
# print(even_numbers)
