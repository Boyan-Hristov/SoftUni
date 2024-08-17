from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS.keys():
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            diver = self.VALID_DIVERS[diver_type](diver_name)
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

        else:
            return f"{diver_name} is already a participant."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH.keys():
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            fish = self.VALID_FISH[fish_type](fish_name, points)
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

        else:
            return f"{fish_name} is already permitted."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level <= 0:
            diver.update_health_status = True

        return message

    def health_recovery(self):
        divers_to_recover = [d for d in self.divers if d.has_health_issue]
        for diver in divers_to_recover:
            diver.update_health_status()
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_to_recover)}"

    def diver_catch_report(self, diver_name: str):
        result = [f"**{diver_name} Catch Report**"]
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        for fish in diver.catch:
            result.append(fish.fish_details())

        return "\n".join(result)

    def competition_statistics(self):
        result = ["**Nautical Catch Challenge Statistics**"]
        for diver in sorted(self.divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name)):
            if not diver.has_health_issue:
                result.append(str(diver))

        return "\n".join(result)
