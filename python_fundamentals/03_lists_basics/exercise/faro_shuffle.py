deck_of_cards = input()
faro_shuffles_count = int(input())

deck_of_cards_list = deck_of_cards.split(" ")

for shuffle in range(faro_shuffles_count):
    half_deck = len(deck_of_cards_list) // 2
    first_half = deck_of_cards_list[:half_deck]
    second_half = deck_of_cards_list[half_deck:]
    shuffled_deck = []
    for i in range(half_deck):
        shuffled_deck.append(first_half[i])
        shuffled_deck.append(second_half[i])
    deck_of_cards_list = shuffled_deck

print(shuffled_deck)
