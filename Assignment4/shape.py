# Q4. Concept: Inheritance and Method Overriding
# Create a class Shape with a method area().
# Create subclasses Circle, Rectangle, and Triangle
# that override the area() method.

import math

# Parent class
class Shape:
    def area(self):
        pass

# Child class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Child class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Child class: Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create objects
circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

# Display areas
print("Area of Circle:", round(circle.area(), 2))
print("Area of Rectangle:", rectangle.area())
print("Area of Triangle:", triangle.area())