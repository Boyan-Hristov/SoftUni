# gifts = input()
# command = input()
#
# gifts_list = gifts.split(" ")
#
# while not command == "No Money":
#
#     if "OutOfStock" in command:
#         command_list = command.split(" ")
#         gift_needed = command_list[1]
#         if gift_needed in gifts_list:
#             gift_to_replace_indices = []
#             for i in range(len(gifts_list)):
#                 if gifts_list[i] == gift_needed:
#                     gift_to_replace_indices.append(gifts_list[i])
#             # gift_to_replace_indices_as_integer = []
#             # for j in gift_to_replace_indices:
#             #     gift_to_replace_indices_as_integer.append(j)
#             for index in gift_to_replace_indices:
#                 index_to_replace = gifts_list.index(gift_needed)
#                 gifts_list[index_to_replace] = "None"
#
#     elif "Required" in command:
#         command_list = command.split(" ")
#         index_to_replace = int(command_list[2])
#         replacement_gift = command_list[1]
#         if index_to_replace < len(gifts_list):
#             gifts_list[index_to_replace] = replacement_gift
#
#     elif "JustInCase" in command:
#         command_list = command.split(" ")
#         replacement_gift = command_list[1]
#         gifts_list[-1] = replacement_gift
#
#     command = input()
#
# for gift in gifts_list:
#     if not gift == "None":
#         print(gift, end=" ")

gifts = input().split()
command = input()

while not command == "No Money":
    command_info = command.split()

    if "OutOfStock" in command:
        gift_to_replace = command_info[1]
        gift_to_replace_indices = []
        for i in range(len(gifts)):
            if gifts[i] == gift_to_replace:
                gifts[i] = "None"

    elif "Required" in command:
        replacement_gift = command_info[1]
        index_to_replace = int(command_info[2])
        if 0 <= index_to_replace < len(gifts):
            gifts[index_to_replace] = replacement_gift

    elif "JustInCase" in command:
        replacement_gift = command_info[1]
        gifts[-1] = replacement_gift

    command = input()

for gift in gifts:
    if not gift == "None":
        print(f"{gift}", end=" ")
