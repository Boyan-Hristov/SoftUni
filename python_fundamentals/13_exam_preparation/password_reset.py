# password = input()
# command = input()
# while not command == "Done":
#     tokens = command.split()
#     action = tokens[0]
#     if action == "TakeOdd":
#         new_password = ""
#         for index in range(len(password)):
#             if index % 2 != 0:
#                 new_password += password[index]
#         password = new_password
#         print(password)
#     elif action == "Cut":
#         index = int(tokens[1])
#         length = int(tokens[2])
#         substring = password[index:index + length]
#         password = password.replace(substring, "", 1)
#         print(password)
#     elif action == "Substitute":
#         substring = tokens[1]
#         substitute = tokens[2]
#         if substring in password:
#             password = password.replace(substring, substitute)
#             print(password)
#         else:
#             print("Nothing to replace!")
#     command = input()
#
# print(f"Your password is: {password}")

password = input()
command = input().split()
while not command[0] == "Done":
    action = command[0]
    if action == "TakeOdd":
        new_password = ""
        for index in range(len(password)):
            if index % 2 != 0:
                new_password += password[index]
        password = new_password
        print(password)
    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)
    elif action == "Substitute":
        substring_to_replace, substitute = command[1], command[2]
        if substring_to_replace in password:
            password = password.replace(substring_to_replace, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input().split()

print(f"Your password is: {password}")
