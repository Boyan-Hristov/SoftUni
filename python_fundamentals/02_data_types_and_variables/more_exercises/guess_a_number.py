from random import randint
computer_number = randint(1, 100)
while True:
    player_guess = input("Guess the number (1-100): ")
    if not player_guess .isdigit():
        print("Invalid input. Try again...")
        continue
    else:
        player_number = int(player_guess)
        if player_number == computer_number:
            print("You guessed it!")
            break
        elif player_number > computer_number:
            print("Too high!")
        else:
            print("Too low!")
