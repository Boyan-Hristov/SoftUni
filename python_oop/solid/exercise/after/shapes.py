from abc import ABC, abstractmethod
from typing import List
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Circle(Shape):

    def __init__(self, radius: int):
        self.radius = radius

    def calculate_area(self):
        return self.radius * (pi ** 2)


class AreaCalculator:

    def __init__(self, shapes: List[Shape]):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Triangle(3, 5), Circle(3), Square(4)]
calculator = AreaCalculator(shapes)
print(f"The total area is: {calculator.total_area:.2f}")
