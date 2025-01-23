from shape import Shape
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.__length = float(length)
        self.__breadth = float(breadth)
    
    def calculate_area(self):
        return self.__length * self.__breadth
    
    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = float(length)
    
    def get_breadth(self):
        return self.__breadth
    
    def set_breadth(self, breadth):
        self.__breadth = float(breadth)
