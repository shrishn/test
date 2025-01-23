import math
from shape import Shape

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * self.radius ** 2
