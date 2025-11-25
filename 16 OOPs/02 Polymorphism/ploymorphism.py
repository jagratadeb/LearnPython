# Base class
class Shape:
    def area(self):
        return f"Area of the shape"
    
# Derived class 1
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

# Derived class 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def xyz(self):
        pass
    
# Derived class 3
class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.height * self.base


# Function with polymorphism
def print_area(shape):
    print(f"The area is {shape.area()}")
    

rectangle = Rectangle(10,5)
circle = Circle(5)
triangle = Triangle(10,5)

print_area(rectangle)
print_area(circle)
print_area(triangle)

