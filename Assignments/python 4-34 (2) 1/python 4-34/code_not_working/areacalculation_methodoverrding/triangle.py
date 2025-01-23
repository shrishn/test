from shape import Shape

class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def calculate_area(self):
        return 0.5 * self.base * self.height
