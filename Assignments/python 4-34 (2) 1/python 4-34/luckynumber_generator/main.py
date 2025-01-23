def find_lucky_number(name, table):
    # Check if the name is in uppercase
    if name.islower():
        yield 0
        return
    
    # Create a dictionary to map characters to their corresponding lucky number values
    char_to_number = dict(zip(table[0], table[1]))
    
    # Calculate the lucky number by summing the values corresponding to each character in the name
    total = 0
    for char in name:
        if char in char_to_number:
            total += char_to_number[char]
        else:
            # If a character is not in the table (e.g., spaces or invalid characters), handle gracefully
            yield 0
            return
    
    yield total  # Yield the calculated lucky number

def main():
    # The table for mapping letters to numbers
    table = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
             [1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3, 4, 5, 7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7]]
    
    # Input name
    name = input("Enter your name: ")
    
    # Call the find_lucky_number function
    lucky_number_generator = find_lucky_number(name.upper(), table)
    
    # Get the lucky number from the generator
    lucky_number = next(lucky_number_generator)
    
    if lucky_number == 0:
        print("Your lucky number is: 0")
        print("Invalid name")
    else:
        print(f"Your lucky number is:{lucky_number}")

if __name__ == '__main__':
    main()
