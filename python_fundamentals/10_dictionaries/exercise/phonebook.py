phonebook = {}
while True:
    command = input()
    if "-" not in command:
        break
    name, phone_number = command.split("-")
    phonebook[name] = phone_number
for i in range(int(command)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
