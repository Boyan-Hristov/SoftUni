from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
