from abc import ABC, abstractmethod


class BaseEquipment(ABC):

    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @property
    @abstractmethod
    def price_increment(self):
        pass

    def increase_price(self):
        self.price *= self.price_increment
