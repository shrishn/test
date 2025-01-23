import math
from shape import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = float(radius)
    
    def calculate_area(self):
        return math.pi * self.__radius ** 2
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = float(radius)