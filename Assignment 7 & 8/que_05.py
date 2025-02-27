# Create a base class "Shape" with methods to calculate the area and perimeter. Implement
# derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
# and perimeter calculations.

import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    shape_type = input("Enter shape type (rectangle/circle): ").strip().lower()
    
    if shape_type == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        shape = Rectangle(length, width)
    elif shape_type == "circle":
        radius = float(input("Enter radius: "))
        shape = Circle(radius)
    else:
        print("Invalid shape type.")
        exit()
    
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())