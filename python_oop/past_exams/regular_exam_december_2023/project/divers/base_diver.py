from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    MIN_OXYGEN_LEVEL = 0
    INITIAL_OXYGEN_LEVEL = 0

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0  # Returns a floating-point number rounded to the first decimal place
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")

        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < BaseDiver.MIN_OXYGEN_LEVEL:
            raise ValueError("Cannot create diver with negative oxygen level!")

        self.__oxygen_level = value

    @property
    @abstractmethod
    def oxygen_level_reducer(self):
        pass

    def miss(self, time_to_catch: int):
        # check if it needs a condition if the result is a float only then to round
        if self.oxygen_level >= time_to_catch:
            self.oxygen_level -= round(time_to_catch * self.oxygen_level_reducer)
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

    def hit(self, fish: BaseFish):
        if self.oxygen_level >= fish.time_to_catch:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += float(f"{fish.points:.1f}")
        else:
            self.oxygen_level = 0

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, " \
               f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]"

