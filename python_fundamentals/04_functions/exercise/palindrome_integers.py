numbers = input().split(", ")


def palindrome(my_list):
    for number in my_list:
        reversed_number = number[::-1]
        if number == reversed_number:
            print(True)
        else:
            print(False)


palindrome(numbers)


# 02
# def is_palindrome(some_number: str) -> bool:
#     return some_number == some_number[::-1]
#
#
# numbers = input().split(", ")
# for number in numbers:
#     print(is_palindrome(number))
