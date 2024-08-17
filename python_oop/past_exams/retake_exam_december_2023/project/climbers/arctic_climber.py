from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 200)

    @property
    def required_strength(self):
        return 100

    @property
    def peak_strength_diminisher(self):
        return {"Extreme": 20 * 2, "Advanced": 20 * 1.5}


