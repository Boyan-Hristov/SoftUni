from guild_system.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, some_player: Player):

        if some_player.guild == self.name:
            return f"Player {some_player.name} is already in the guild."

        elif not some_player.guild == self.name and not some_player.guild == some_player.DEFAULT_GUILD:
            return f"Player {some_player.name} is in another guild."

        self.players.append(some_player)
        some_player.guild = self.name
        return f"Welcome player {some_player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            current_player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(current_player)
        current_player.guild = current_player.DEFAULT_GUILD
        return f"Player {player_name} has been removed from the guild."
        # for current_player in self.players:
        #     if current_player.name == player_name:
        #         self.players.remove(current_player)
        #         current_player.guild = "Unaffiliated"
        #         return f"Player {player_name} has been removed from the guild."
        # else:
        #     return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = ["", f"Guild: {self.name}"]
        for current_player in self.players:
            info.append(current_player.player_info())

        return "\n".join(info)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
