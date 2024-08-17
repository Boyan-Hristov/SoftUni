class Controller:
    VALID_SUSTENANCE = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        valid_players = [p for p in args if p not in self.players]
        self.players.extend(valid_players)
        return f"Successfully added: {', '.join([p.name for p in valid_players])}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return

        if sustenance_type not in self.VALID_SUSTENANCE:
            return
        # check if it works
        if not player.need_sustenance:
            raise Exception(f"{player_name} have enough stamina.")
        # check if it works
        sustenance_available = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]
        if not sustenance_available:
            return f"There are no {sustenance_type.lower()} supplies left!"

        supply = sustenance_available[-1]
        player.stamina = min(player.MAX_STAMINA, player.stamina + supply.energy)
        # check if second -1 should be 0
        for i in range(len(self.supplies) - 1, 0, -1):
            if self.supplies[i] == supply:
                self.supplies.pop(i)
                break

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = next(filter(lambda p: p.name == first_player_name, self.players))
        player_two = next(filter(lambda p: p.name == second_player_name, self.players))

        message = []
        weak_players = [p for p in (player_one, player_two) if p.stamina == 0]
        if weak_players:
            # check if format is valid
            message.extend([f"Player {p.name} does not have enough stamina." for p in weak_players])
            return "\n".join(message)

        players = sorted([player_one, player_two], key=lambda p: p.stamina)
        first_player, second_player = players

        first_player_damage = first_player.stamina / 2

        second_player.stamina -= first_player_damage
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"

        second_player_damage = second_player.stamina / 2
        first_player.stamina -= second_player_damage
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {second_player.name}"

        winner = sorted([first_player, second_player], key=lambda p: -p.stamina)[0]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = [str(p) for p in self.players]
        result.extend([s.details() for s in self.supplies])
        return "\n".join(result)
