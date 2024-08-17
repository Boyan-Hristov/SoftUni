coffee_counter = 0
while True:
    command = input()
    if command == "END":
        break
    else:
        if command.lower() == "coding" \
        or command.lower() == "dog" \
        or command.lower() == "cat" \
        or command.lower() == "movie":
            if command.islower():
                coffee_counter += 1
            elif command.isupper():
                coffee_counter += 2
if coffee_counter <= 5:
    print(coffee_counter)
else:
    print("You need extra sleep")