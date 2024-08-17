sequence = input().split()
command = input()
moves = 0
while command != "end":
    command_list = [int(s) for s in command.split()]
    first_index = command_list[0]
    second_index = command_list[1]
    if first_index == second_index or \
            (first_index not in range(len(sequence)) or second_index not in range(len(sequence))):
        moves += 1
        sequence_middle = len(sequence) // 2
        sequence.insert(sequence_middle, f"-{moves}a")
        sequence.insert(sequence_middle, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence[first_index] == sequence[second_index]:
        moves += 1
        element = sequence[first_index]
        sequence = [s for s in sequence if s != sequence[first_index]]
        print(f"Congrats! You have found matching elements - {element}!")

    elif sequence[first_index] != sequence[second_index]:
        moves += 1
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()

if len(sequence) > 0:
    print(f"Sorry you lose :( \n"
          f"{' '.join(sequence)}")



