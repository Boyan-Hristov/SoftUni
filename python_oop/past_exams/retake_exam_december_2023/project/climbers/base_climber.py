from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    MIN_STRENGTH = 0

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Climber name cannot be null or empty!")

        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= BaseClimber.MIN_STRENGTH:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")

        self.__strength = value

    @property
    @abstractmethod
    def required_strength(self):
        pass

    @property
    @abstractmethod
    def peak_strength_diminisher(self):
        pass

    def can_climb(self):
        # check if it works as and ordinary method, not abstract
        return self.strength >= self.required_strength

    def climb(self, peak: BasePeak):
        # check if it works as an ordinary method, not abstract
        # again check if the setter works as expected
        self.strength -= self.peak_strength_diminisher[peak.difficulty_level]
        self.conquered_peaks.append(peak.name)

    def rest(self):
        # debug and check if code works as expected
        # if not, try to change to "self.__strength += 15"
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.__name__}: " \
               f"/// Climber name: {self.name} * Left strength: {self.strength:.1f} * " \
               f"Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///"
