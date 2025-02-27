# Create a class for representing any 2-D point or vector. The methods inside this class include
# its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
# calculating the distance between two vectors, dot product, cross product of two vectors. Extend
# the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
# D.

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

if __name__ == "__main__":
    x1 = float(input("Enter x for first 2D vector: "))
    y1 = float(input("Enter y for first 2D vector: "))
    x2 = float(input("Enter x for second 2D vector: "))
    y2 = float(input("Enter y for second 2D vector: "))
    v1 = Vector2D(x1, y1)
    v2 = Vector2D(x2, y2)
    print("Distance:", v1.distance(v2))
    print("Dot Product:", v1.dot_product(v2))
    print("Cross Product:", v1.cross_product(v2))
    
    x3 = float(input("Enter x for first 3D vector: "))
    y3 = float(input("Enter y for first 3D vector: "))
    z3 = float(input("Enter z for first 3D vector: "))
    x4 = float(input("Enter x for second 3D vector: "))
    y4 = float(input("Enter y for second 3D vector: "))
    z4 = float(input("Enter z for second 3D vector: "))
    v3 = Vector3D(x3, y3, z3)
    v4 = Vector3D(x4, y4, z4)
    print("Distance:", v3.distance(v4))
    print("Dot Product:", v3.dot_product(v4))
    cross = v3.cross_product(v4)
    print("Cross Product:", (cross.x, cross.y, cross.z))