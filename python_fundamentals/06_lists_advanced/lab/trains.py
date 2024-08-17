def train(command: str) -> list:
    command_info = command.split()
    if "add" in command:
        wagons_list[-1] += int(command_info[1])
    elif "insert" in command:
        wagons_list[int(command_info[1])] += int(command_info[2])
    elif "leave" in command:
        wagons_list[int(command_info[1])] -= int(command_info[2])
    return wagons_list


number_of_wagons = int(input())
wagons_list = [0] * number_of_wagons
current_command = input()

while True:
    if current_command == "End":
        break
    else:
        train(current_command)
    current_command = input()

print(train(current_command))




