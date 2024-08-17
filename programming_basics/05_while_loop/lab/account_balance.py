command = input()
total_sum = 0
while command != "NoMoreMoney":
    command_value = float(command)
    if command_value < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {command_value:.2f}")
    total_sum += command_value
    command = input()

print(f"Total: {total_sum:.2f}")



