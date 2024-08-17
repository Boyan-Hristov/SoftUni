from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        print("meow")


class Dog(Animal):

    def make_sound(self):
        print("woof-woof")


class Chicken(Animal):

    def make_sound(self):
        print("pio")


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
for animal in animals:
    animal.make_sound()
