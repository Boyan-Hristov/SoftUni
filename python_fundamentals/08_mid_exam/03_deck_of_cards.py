# cards = input().split(", ")
# number = int(input())
#
# for i in range(number):
#     command = input().split(", ")
#     action = command[0]
#     if action == "Add":
#         card_to_add = command[1]
#         if card_to_add in cards:
#             print("Card is already in the deck")
#         else:
#             cards.append(card_to_add)
#             print("Card successfully added")
#     elif action == "Remove":
#         card_to_remove = command[1]
#         if card_to_remove not in cards:
#             print("Card not found")
#         else:
#             cards.remove(card_to_remove)
#             print("Card successfully removed")
#     elif action == "Remove At":
#         index_to_remove = int(command[1])
#         if 0 <= index_to_remove < len(cards):
#             cards.pop(index_to_remove)
#             print("Card successfully removed")
#         else:
#             print("Index out of range")
#     elif action == "Insert":
#         index_to_insert = int(command[1])
#         card_to_insert = command[2]
#         if 0 <= index_to_insert < len(cards):
#             if card_to_insert in cards:
#                 print("Card is already added")
#             else:
#                 cards.insert(index_to_insert, card_to_insert)
#                 print("Card successfully added")
#         else:
#             print("Index out of range")
#
# print(", ".join(cards))


def add(card: str, deck: list) -> list:
    if card in deck:
        print("Card is already in the deck")
    else:
        deck.append(card)
        print("Card successfully added")
    return deck


def remove(card: str, deck: list) -> list:
    if card not in deck:
        print("Card not found")
    else:
        deck.remove(card)
        print("Card successfully removed")
    return deck


def remove_at(index: int, deck: list) -> list:
    if 0 <= index < len(deck):
        deck.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")
    return deck


def insert(index: int, card_to_insert: str, deck: list) -> list:
    if 0 <= index < len(deck):
        if card_to_insert not in deck:
            deck.insert(index, card_to_insert)
            print("Card successfully added")

        else:
            print("Card is already added")
    else:
        print("Index out of range")
    return deck


cards = input().split(", ")
number = int(input())

for i in range(number):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        cards = add(command[1], cards)
    elif action == "Remove":
        cards = remove(command[1], cards)
    elif action == "Remove At":
        cards = remove_at(int(command[1]), cards)
    elif action == "Insert":
        cards = insert(int(command[1]), command[2], cards)

print(", ".join(cards))
