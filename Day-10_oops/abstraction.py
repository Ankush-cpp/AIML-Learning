# Day 10: Abstraction Example

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Objects
r = Rectangle(5, 4)
c = Circle(3)

print("Rectangle area:", r.area())
print("Circle area:", c.area())