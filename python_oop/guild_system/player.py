class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name: str, mana_cost: int):
        if self.skills.get(skill_name):
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
        ]
        info.extend(list({f"==={key} - {value}" for key, value in self.skills.items()}))

        return "\n".join(info)

