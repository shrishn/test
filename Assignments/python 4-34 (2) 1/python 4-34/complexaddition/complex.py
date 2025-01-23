class Addition:
    def __init__(self):
        self.__real = 0
        self.__img = 0
        
    def get_real(self):
        return self.__real
        
    def set_real(self, real):
        self.__real = real
        
    def get_img(self):
        return self.__img
        
    def set_img(self, img):
        self.__img = img 
    
    def addRealPart(self, obj1, obj2):
        # Add real parts of two complex numbers
        return obj1.get_real() + obj2.get_real()
   
    def addImaginaryPart(self, obj1, obj2):
        # Add imaginary parts of two complex numbers
        return obj1.get_img() + obj2.get_img()
    
    def __add__(self, oth_obj):
        # Overload the + operator to add two complex numbers
        real_sum = self.get_real() + oth_obj.get_real()
        img_sum = self.get_img() + oth_obj.get_img()
        
        # Create a new Addition object to store the result
        result = Addition()
        result.set_real(real_sum)
        result.set_img(img_sum)
        
        return result
    
    def __str__(self):
        # Return the complex number in the format: real + imaginary i
        return f"{self.get_real()} + {self.get_img()}i"
 
def main():
    # Get inputs for the first complex number
    print("Enter the real and imaginary parts of the first complex number:")
    real1 = int(input())
    img1 = int(input())
    
    # Get inputs for the second complex number
    print("Enter the real and imaginary parts of the second complex number:")
    real2 = int(input())
    img2 = int(input())
    
    # Create objects for the two complex numbers
    complex1 = Addition()
    complex1.set_real(real1)
    complex1.set_img(img1)
    
    complex2 = Addition()
    complex2.set_real(real2)
    complex2.set_img(img2)
    
    # Add real parts and imaginary parts using methods
    real_sum = complex1.addRealPart(complex1, complex2)
    img_sum = complex1.addImaginaryPart(complex1, complex2)
    
    print(f"Real part addition: {real_sum}")
    print(f"Imaginary part addition: {img_sum}")
    
    # Add the two complex numbers using operator overloading
    result = complex1 + complex2
    print(f"Complex Number: {result}")
 
if __name__ == "__main__":
    main()
