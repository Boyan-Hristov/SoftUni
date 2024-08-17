red_cards = input()
red_cards_list = red_cards.split(" ")

team_a_red_cards = []
team_b_red_cards = []

team_a_players = 11
team_b_players = 11

is_game_terminated = False

for card in red_cards_list:
    if card in team_a_red_cards or card in team_b_red_cards:
        continue
    if "A" in card:
        team_a_red_cards.append(card)
    elif "B" in card:
        team_b_red_cards.append(card)
    if team_a_players - len(team_a_red_cards) < 7 or team_b_players - len(team_b_red_cards) < 7:
        is_game_terminated = True
        break

team_a_remaining_players = team_a_players - len(team_a_red_cards)
team_b_remaining_players = team_b_players - len(team_b_red_cards)

print(f"Team A - {team_a_remaining_players}; Team B - {team_b_remaining_players}")

if is_game_terminated:
    print("Game was terminated")