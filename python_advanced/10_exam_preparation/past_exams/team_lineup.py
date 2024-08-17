def team_lineup(*args) -> str:
    result = ""
    players = {}

    for pair in args:
        if pair[1] not in players.keys():
            players[pair[1]] = []
        players[pair[1]].append(pair[0])

    players = dict(sorted(players.items(), key=lambda x: (-len(x[1]), x[0])))
    for country, names in players.items():
        result += f"{country}:\n"
        for player in names:
            result += f"  -{player}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


