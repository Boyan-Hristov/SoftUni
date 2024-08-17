# pieces = {}
# number_of_pieces = int(input())
# for info in range(number_of_pieces):
#     piece, composer, key = input().split("|")
#     pieces[piece] = {"composer": composer, "key": key}
#
# command = input().split("|")
# while not command[0] == "Stop":
#     action = command[0]
#     if action == "Add":
#         new_piece, new_composer, new_key = command[1], command[2], command[3]
#         if new_piece not in pieces.keys():
#             pieces[new_piece] = {"composer": new_composer, "key": new_key}
#             print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
#         else:
#             print(f"{new_piece} is already in the collection!")
#     elif action == "Remove":
#         piece_to_remove = command[1]
#         if piece_to_remove in pieces.keys():
#             pieces.pop(piece_to_remove)
#             print(f"Successfully removed {piece_to_remove}!")
#         else:
#             print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
#     elif action == "ChangeKey":
#         piece_to_change, changed_key = command[1], command[2]
#         if piece_to_change in pieces.keys():
#             pieces[piece_to_change]["key"] = changed_key
#             print(f"Changed the key of {piece_to_change} to {changed_key}!")
#         else:
#             print(f"Invalid operation! {piece_to_change} does not exist in the collection.")
#     command = input().split("|")
#
# for some_piece, information in pieces.items():
#     print(f"{some_piece} -> Composer: {information['composer']}, Key: {information['key']}")


pieces = {}
number_of_pieces = int(input())
for current_piece in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}
command = input().split("|")
while not command[0] == "Stop":
    action = command[0]
    if action == "Add":
        new_piece, new_composer, new_key = command[1], command[2], command[3]
        if new_piece not in pieces.keys():
            pieces[new_piece] = {"composer": new_composer, "key": new_key}
            print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
        else:
            print(f"{new_piece} is already in the collection!")
    elif action == "Remove":
        piece_to_remove = command[1]
        if piece_to_remove in pieces.keys():
            pieces.pop(piece_to_remove)
            print(f"Successfully removed {piece_to_remove}!")
        else:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    elif action == "ChangeKey":
        piece_to_change, changed_key = command[1], command[2]
        if piece_to_change in pieces.keys():
            pieces[piece_to_change]["key"] = changed_key
            print(f"Changed the key of {piece_to_change} to {changed_key}!")
        else:
            print(f"Invalid operation! {piece_to_change} does not exist in the collection.")
    command = input().split("|")

for extracted_piece, information in pieces.items():
    print(f"{extracted_piece} -> Composer: {information['composer']}, Key: {information['key']}")
