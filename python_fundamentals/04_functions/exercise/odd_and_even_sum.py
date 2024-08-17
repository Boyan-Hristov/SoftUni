integer = int(input())


def odd_even_sum(number):
    number_as_string = str(number)
    even_digits = []
    odd_digits = []
    for digit in number_as_string:
        if int(digit) % 2 == 0:
            even_digits.append(int(digit))
        else:
            odd_digits.append(int(digit))
    even_digits_sum = sum(even_digits)
    odd_digits_sum = sum(odd_digits)
    return f"Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}"


print(odd_even_sum(integer))


# 02
# def odd_even_sum(some_number: str) -> int and int:
#     sum_of_even = 0
#     sum_of_odd = 0
#     for digit in some_number:
#         if int(digit) % 2 == 0:
#             sum_of_even += int(digit)
#         else:
#             sum_of_odd += int(digit)
#     return sum_of_odd, sum_of_even       # return може да връща повече от една стойност
#
#
# number = input()
# sum_of_odd_digits, sum_of_even_digits = odd_even_sum(number)
# print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
