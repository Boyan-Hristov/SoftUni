# encrypted_message = input()
# command = input()
# while command != "Decode":
#     command_info = command.split("|")
#     action = command_info[0]
#     if action == "Move":
#         substring = ""
#         number_of_letters = int(command_info[1])
#         for index in range(0, number_of_letters):
#             substring += encrypted_message[index]
#         # encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
#         encrypted_message = encrypted_message.replace(substring, "")
#         encrypted_message += substring
#     elif action == "Insert":
#         index = int(command_info[1])
#         value = command_info[2]
#         encrypted_message = f"{encrypted_message[:index]}{value}{encrypted_message[index:]}"
#     elif action == "ChangeAll":
#         substring = command_info[1]
#         replacement = command_info[2]
#         while substring in encrypted_message:
#             encrypted_message = encrypted_message.replace(substring, replacement, 1)
#     command = input()
# print(f"The decrypted message is: {encrypted_message}")


message = input()
command = input().split("|")
while not command[0] == "Decode":
    action = command[0]
    if action == "Move":
        number_of_letters = int(command[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif action == "Insert":
        index, value = int(command[1]), command[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        if substring in message:
            message = message.replace(substring, replacement)
    command = input().split("|")
print(f"The decrypted message is: {message}")
