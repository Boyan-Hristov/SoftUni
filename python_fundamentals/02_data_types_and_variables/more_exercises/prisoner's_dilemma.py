from random import randint
defect = "Defect"
cooperate = "Cooperate"
while True:
    player_choice = input("Choose [d]efect or [c]ooperate: ")
    if player_choice == "d":
        player_choice = defect
    elif player_choice == "c":
        player_choice = cooperate
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_choice = randint(1, 2)
    if computer_choice == 1:
        computer_choice = defect
    else:
        computer_choice = cooperate

    print(f"The computer chose to {computer_choice}")

    if player_choice == defect and computer_choice == defect:
        print("You both serve 3 years in prison!")
    elif player_choice == defect and computer_choice == cooperate:
        print("You are set free and the computer serves 5 years in computer prison!")
    elif player_choice == cooperate and computer_choice == defect:
        print("You serve 5 years in prison and the computer is set free!")
    elif player_choice == cooperate and computer_choice == cooperate:
        print("You both serve 1 year in prison!")

    replay = input("Type [yes] to play again or [no] to quit: ")
    if replay == "no":
        break

