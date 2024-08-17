from abc import ABC, abstractmethod


class BasePeak(ABC):
    NAME_MIN_SYMBOLS = 2
    MIN_ELEVATION = 1500

    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < BasePeak.NAME_MIN_SYMBOLS:
            raise ValueError("Peak name cannot be less than 2 symbols!")

        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value):
        if value < BasePeak.MIN_ELEVATION:
            raise ValueError("Peak elevation cannot be below 1500m.")

        self.__elevation = value

    @abstractmethod
    def calculate_difficulty_level(self):
        pass

    @abstractmethod
    def get_recommended_gear(self):
        pass
