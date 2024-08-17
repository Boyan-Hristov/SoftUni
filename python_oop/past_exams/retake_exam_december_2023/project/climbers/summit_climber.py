from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 150)

    @property
    def required_strength(self):
        return 75

    @property
    def peak_strength_diminisher(self):
        return {"Extreme": 30 * 2.5, "Advanced": 30 * 1.3}

