# Import necessary module here
from pattern import generate_pattern

def main():
    # Write your code here
    input_pattern = input("Enter the input text: ")
    length = int(input("Enter the length of each row: "))
    
    # Call the generate_pattern function and print the result
    result = generate_pattern(input_pattern, length)
    print(result)
    
    return

if __name__ == '__main__':
    main()
