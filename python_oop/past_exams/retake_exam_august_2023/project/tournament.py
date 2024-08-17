from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT.keys():
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS.keys():
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment = self.VALID_EQUIPMENT[equipment_type]
        if team.budget < equipment.PRICE:
            raise Exception("Budget is not enough!")

        for i in range(len(self.equipment) - 1, -1, -1):
            if self.equipment[i].PRICE == equipment.PRICE:
                sold_equipment = self.equipment[i]
                team.equipment.append(sold_equipment)
                team.budget -= sold_equipment.PRICE
                self.equipment.pop(i)
                break

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_count = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                equipment_count += 1
                e.increase_price()
        return f"Successfully changed {equipment_count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team_2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if not team_1.__class__.__name__ == team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_result = team_1.advantage + sum([e.PROTECTION for e in team_1.equipment])
        team_2_result = team_2.advantage + sum([e.PROTECTION for e in team_2.equipment])

        if team_1_result > team_2_result:
            team_1.win()
            return f"The winner is {team_name1}."
        elif team_2_result > team_1_result:
            team_2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:"]
        for team in sorted(self.teams, key=lambda x: -x.wins):
            result.append(team.get_statistics())

        return "\n".join(result)
