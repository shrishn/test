# Define the function to generate the pattern
def generate_pattern(input_pattern, length):
    # Check for invalid row length
    if length <= 0:
        return "Invalid input. Please provide a positive row length"
    
    # Initialize an empty string to store the generated pattern
    pattern = ""
    
    # Loop to create the pattern
    for i in range(length):
        # Use slicing to create each row based on the pattern
        row = input_pattern[i:] + input_pattern[:i]  # Shift the pattern by one character each time
        pattern += row[:length] + "\n"  # Add the row to the pattern, ensuring it doesn't exceed the specified length
    
    # Return the generated pattern without leading/trailing whitespace
    return pattern.strip()