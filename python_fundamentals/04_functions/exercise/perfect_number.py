integer = int(input())


def perfect_number(number: int) -> str:
    is_perfect = False
    divisors = []
    for current_number in range(1, number):
        if number % current_number == 0:
            divisors.append(current_number)
    divisors_sum = sum(divisors)
    if number == divisors_sum:
        is_perfect = True
    if is_perfect:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(integer))


# integer = int(input())
#
#
# def perfect_number(number):
#     is_perfect = False
#     divisors = []
#     for current_number in range(1, number + 1):
#         if number % current_number == 0:
#             divisors.append(current_number)
#     divisors_sum = sum(divisors)
#     if number == divisors_sum // 2:
#         is_perfect = True
#     if is_perfect:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# print(perfect_number(integer))
