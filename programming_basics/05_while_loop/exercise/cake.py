width = int(input())
length = int(input())
command = input()

total_pieces = width * length
pieces_taken = 0
pieces_needed = 0
is_finished = False
while not command == "STOP":
    current_pieces = int(command)
    pieces_taken += current_pieces
    if pieces_taken > total_pieces:
        pieces_needed = pieces_taken - total_pieces
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        is_finished = True
        break
    command = input()

if not is_finished:
    pieces_left = total_pieces - pieces_taken
    print(f"{pieces_left} pieces are left.")