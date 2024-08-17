# message = input()
# command = input()
# while not command == "Reveal":
#     tokens = command.split(":|:")
#     action = tokens[0]
#     if action == "InsertSpace":
#         index = int(tokens[1])
#         message = message[:index] + " " + message[index:]
#         print(message)
#     elif action == "Reverse":
#         substring = tokens[1]
#         if substring in message:
#             message = message.replace(substring, "", 1)
#             reversed_substring = substring[::-1]
#             message = message + reversed_substring
#             print(message)
#         else:
#             print("error")
#     elif action == "ChangeAll":
#         substring = tokens[1]
#         replacement = tokens[2]
#         if substring in message:
#             message = message.replace(substring, replacement)
#             print(message)
#     command = input()
#
# print(f"You have a new text message: {message}")

message = input()
command = input().split(":|:")
while not command[0] == "Reveal":
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring_to_replace, replacement = command[1], command[2]
        message = message.replace(substring_to_replace, replacement)
        print(message)
    command = input().split(":|:")

print(f"You have a new text message: {message}")
