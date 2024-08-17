from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CARS = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CARS.keys():
            return

        try:
            next(filter(lambda c: c.model == model, self.cars))
            raise Exception(f"Car {model} is already created!")

        except StopIteration:
            car = self.VALID_CARS[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        try:
            next(filter(lambda d: d.name == driver_name, self.drivers))
            raise Exception(f"Driver {driver_name} is already created!")

        except StopIteration:
            driver = Driver(driver_name)
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        try:
            next(filter(lambda r: r.name == race_name, self.races))
            raise Exception(f"Race {race_name} is already created!")

        except StopIteration:
            race = Race(race_name)
            self.races.append(race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type not in self.VALID_CARS.keys():
            raise Exception(f"Car {car_type} could not be found!")

        available_cars = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if not available_cars:
            raise Exception(f"Car {car_type} could not be found!")

        car = available_cars[-1]
        if driver.car is not None:
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            # check
            old_car.is_taken = False
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")
        # check
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda d: -d.car.speed_limit)[:3]
        message = []
        for winner in winners:
            message.append(f"Driver {winner.name} wins the {race_name} "
                           f"race with a speed of {winner.car.speed_limit}.")
            winner.number_of_wins += 1

        return "\n".join(message)
