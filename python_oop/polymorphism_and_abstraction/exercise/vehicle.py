from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def air_conditioner_on(self):
        pass

    def drive(self, distance: int):
        fuel_needed = (self.fuel_consumption + self.air_conditioner_on) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):

    @property
    def air_conditioner_on(self):
        return 0.9

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    REFUEL_KEPT_RATIO = 0.95

    @property
    def air_conditioner_on(self):
        return 1.6

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.REFUEL_KEPT_RATIO


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)



