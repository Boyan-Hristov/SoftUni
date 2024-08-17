from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def gained_weight(self):
        return 0.10

    @property
    def foods(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    @property
    def gained_weight(self):
        return 0.40

    @property
    def foods(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):

    @property
    def gained_weight(self):
        return 0.30

    @property
    def foods(self):
        return [Vegetable, Meat]

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    @property
    def gained_weight(self):
        return 1.00

    @property
    def foods(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"
