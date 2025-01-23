from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
def main():
    shape_type = input("Enter the type of shape: ").strip().lower()
    
    if shape_type == "circle":
        radius = float(input("Enter the radius: "))
        shape = Circle(radius)
    elif shape_type == "rectangle":
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        shape = Rectangle(length, breadth)
    elif shape_type == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        shape = Triangle(base, height)
    else:
        print("Invalid shape type")
        return
    
    area = shape.calculate_area()
    print(f"The area of the {shape_type.capitalize()} is: {area:.2f}")

if __name__ == "__main__":
    main()