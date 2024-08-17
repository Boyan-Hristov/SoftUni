player_name = input()
best_player_goals = 0
best_player = ""
hat_trick = False
while not player_name == "END":
    goals_scored = int(input())
    if goals_scored > best_player_goals:
        best_player_goals = goals_scored
        best_player = player_name
    if goals_scored >= 3:
        hat_trick = True
    if goals_scored >= 10:
        break
    player_name = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")