from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1_000.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)

    @property
    def increase_team_advantage(self):
        return 115


