# import sys
#
#
# def push(some_number: int, some_list: list) -> list:
#     some_list.append(some_number)
#     return some_list
#
#
# def delete(some_list: list) -> list:
#     if some_list:
#         some_list.pop()
#     return some_list
#
#
# def maximum(some_list: list) -> int:
#     max_number = - sys.maxsize
#     for _ in range(len(some_list)):
#         top_element = some_list.pop()
#         some_list.insert(0, top_element)
#         if top_element > max_number:
#             max_number = top_element
#     return max_number
#
#
# def minimum(some_list: list) -> int:
#     min_number = sys.maxsize
#     for _ in range(len(some_list)):
#         top_element = some_list.pop()
#         some_list.insert(0, top_element)
#         if top_element < min_number:
#             min_number = top_element
#     return min_number
#
#
# stack = []
# number_of_lines = int(input())
#
# for i in range(number_of_lines):
#     query = input().split()
#     if query[0] == "1":
#         number_to_push = int(query[1])
#         stack = push(number_to_push, stack)
#     elif query[0] == "2":
#         stack = delete(stack)
#     elif query[0] == "3":
#         print(maximum(stack))
#     elif query[0] == "4":
#         print(minimum(stack))
#
# reversed_stack = []
# for _ in range(len(stack)):
#     reversed_stack.append(stack.pop())
# print(* reversed_stack, sep=", ")


numbers = []
for i in range(int(input())):
    data = input().split()
    command = data[0]
    if command == "1":
        numbers.append(data[1])
    elif command == "2":
        if numbers:
            numbers.pop()
    elif command == "3":
        if numbers:
            print(max(numbers))
    elif command == "4":
        if numbers:
            print(min(numbers))

numbers.reverse()
print(*numbers, sep=", ")
