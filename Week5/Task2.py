# Implement a class hierarchy to represent geometric
#  shapes (e.g., Circle, Rectangle, Triangle) with methods to
#  calculate area and perimeter.

import math
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # For simplicity, assume it's an equilateral triangle
        return 3 * self.base
    
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 5)

    shapes = [circle, rectangle, triangle]

    for shape in shapes:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")