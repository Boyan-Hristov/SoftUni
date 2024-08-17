players = {}
while True:
    command = input()
    if command == "Season end":
        break
    if "->" in command:
        player, position, skill = command.split(" -> ")
        if player not in players.keys():
            players[player] = {}
            players[player][position] = int(skill)
        elif player in players.keys() and position not in players[player].keys():
            players[player][position] = int(skill)
        elif player in players.keys() and position in players[player].keys():
            if int(skill) > players[player][position]:
                players[player][position] = int(skill)
    else:
        player_one, player_two = command.split(" vs ")
        if player_one in players.keys() and player_two in players.keys():
            intersection = False
            for key in players[player_one].keys():
                if key in players[player_two].keys():
                    intersection = True
            if intersection:
                player_one_total_skill = 0
                player_two_total_skill = 0
                for (skill_one, skill_two) in zip(players[player_one].values(), players[player_two].values()):
                    player_one_total_skill += skill_one
                    player_two_total_skill += skill_two
                if player_one_total_skill > player_two_total_skill:
                    players.pop(player_two)
                elif player_two_total_skill > player_one_total_skill:
                    players.pop(player_one)
# players = dict(sorted(players.items(), key=lambda x: (-x[1], x[0])))
players = dict(sorted(players.items(), key=lambda x: x[0]))
players = dict(sorted(players.items(), key=lambda x: sum(x[1].values()), reverse=True))
for player, skill in players.items():
    print(f"{player}: {sum(skill.values())} skill")
    # skill = dict(sorted(skill.items(), key=lambda x: (-x[1], x[0])))
    skill = dict(sorted(skill.items(), key=lambda x: x[0]))
    skill = dict(sorted(skill.items(), key=lambda x: -x[1]))
    for position, points in skill.items():
        print(f"- {position} <::> {points}")



