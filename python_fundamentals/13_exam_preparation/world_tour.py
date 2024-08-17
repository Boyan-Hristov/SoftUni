# def add_stop(string: str, index: int, stop: str) -> str:
#     if index in range(len(string)):
#         string = string[:index] + stop + string[index:]
#     return string
#
#
# def remove_stop(string: str, start_index: int, end_index: int) -> str:
#     if start_index in range(len(string)) and end_index in range(len(string)):
#         string = string[:start_index] + string[end_index + 1:]
#     return string
#
#
# def switch(string: str, old_string: str, new_string: str) -> str:
#     if old_string in string:
#         string = string.replace(old_string, new_string)
#     return string
#
#
# destinations = input()
# command = input()
# while not command == "Travel":
#     tokens = command.split(":")
#     action = tokens[0]
#     if action == "Add Stop":
#         destinations = add_stop(destinations, int(tokens[1]), tokens[2])
#     elif action == "Remove Stop":
#         destinations = remove_stop(destinations, int(tokens[1]), int(tokens[2]))
#     elif action == "Switch":
#         destinations = switch(destinations, tokens[1], tokens[2])
#     print(destinations)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {destinations}")


stops = input()
command = input().split(":")
while not command[0] == "Travel":
    action = command[0]
    if action == "Add Stop":
        index, string = int(command[1]), command[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")
