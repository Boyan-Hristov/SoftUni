number_of_commands = int(input())
users = {}
for i in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in users.keys():
            print(f"ERROR: already registered with plate number {users[username]}")
        else:
            users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username in users.keys():
            users.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for key, value in users.items():
    print(f"{key} => {value}")
