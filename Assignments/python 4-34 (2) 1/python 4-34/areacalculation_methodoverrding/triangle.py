from shape import Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.__base = float(base)
        self.__height = float(height)
    
    def calculate_area(self):
        return 0.5 * self.__base * self.__height
    
    def get_base(self):
        return self.__base
    
    def set_base(self, base):
        self.__base = float(base)
    
    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = float(height)