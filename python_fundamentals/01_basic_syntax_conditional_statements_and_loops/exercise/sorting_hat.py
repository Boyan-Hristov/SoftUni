sorting_successful = True
while True:
    command = input()
    if command == "Welcome!":
        break
    elif command == "Voldemort":
        print("You must not speak of that name!")
        sorting_successful = False
        break
    else:
        if len(command) < 5:
            print(f"{command} goes to Gryffindor.")
        elif len(command) == 5:
            print(f"{command} goes to Slytherin.")
        elif len(command) == 6:
            print(f"{command} goes to Ravenclaw.")
        else:
            print(f"{command} goes to Hufflepuff.")
if sorting_successful:
    print("Welcome to Hogwarts.")