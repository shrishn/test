from shape import Shape

class Rectangle(Shape):
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def calculate_area(self):
        return self.length * self.breadth
