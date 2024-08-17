# first_sequence = {int(x) for x in input().split()}
# second_sequence = {int(x) for x in input().split()}
#
# number_of_lines = int(input())
#
# for _ in range(number_of_lines):
#     tokens = input().split()
#     command, sequence = tokens[0], tokens[1]
#     if not command == "Check":
#         for index in range(2, len(tokens)):
#             number = int(tokens[index])
#             if command == "Add":
#                 if sequence == "First":
#                     first_sequence.add(number)
#                 elif sequence == "Second":
#                     second_sequence.add(number)
#             elif command == "Remove":
#                 if sequence == "First":
#                     if number in first_sequence:
#                         first_sequence.remove(number)
#                 elif sequence == "Second":
#                     if number in second_sequence:
#                         second_sequence.remove(number)
#     else:
#         print(first_sequence.issubset(second_sequence) or first_sequence.issuperset(second_sequence))
#
#
# print(*sorted(first_sequence), sep=", ")
# print(*sorted(second_sequence), sep=", ")



