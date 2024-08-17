from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def gained_weight(self):
        return 0.25

    @property
    def foods(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def gained_weight(self):
        return 0.35

    @property
    def foods(self):
        return [Vegetable, Fruit, Meat, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"

