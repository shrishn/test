from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

def main():
    shape_type = input("Enter the type of shape: ").lower()
    
    if shape_type == "circle":
        radius = float(input("Enter the radius: "))
        shape = Circle(radius)
        area = shape.calculate_area()
        print(f"The area of Circle is: {area:.2f}")
        
    elif shape_type == "rectangle":
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        shape = Rectangle(length, breadth)
        area = shape.calculate_area()
        print(f"The area of the Rectangle is: {area:.2f}")
        
    elif shape_type == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        shape = Triangle(base, height)
        area = shape.calculate_area()
        print(f"The area of Triangle is: {area:.2f}")
        
    else:
        print("Invalid shape type!")

if __name__ == "__main__":
    main()
