from abc import ABC


class Car(ABC):
    MODEL_MIN_LENGTH = 4
    MIN_SPEED = 0
    MAX_SPEED = 0

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < self.MODEL_MIN_LENGTH:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        # check <= and >
        if value < self.MIN_SPEED or value > self.MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED} and {self.MAX_SPEED}!")
        self.__speed_limit = value
