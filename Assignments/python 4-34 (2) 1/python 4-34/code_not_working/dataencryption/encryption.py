import re

def encrypt_message(message):
    # Function to shift a character to the next character
    def shift_char(char):
        if char.isalpha():  # Only shift alphabetic characters
            if char.lower() == 'z':
                return 'a' if char.islower() else 'A'
            elif char.lower() == 'Z':
                return 'A'
            else:
                return chr(ord(char) + 1)
        return char  # Non-alphabetic characters remain the same
    
    # Use regular expression to process the string character by character
    encrypted_message = ''.join(shift_char(c) for c in message)
    
    return encrypted_message

def main():
    # Sample Input 1
    message1 = "Jai"
    print("Actual message:", message1)
    print("Encrypted message:", encrypt_message(message1))
    
    # Sample Input 2
    message2 = "say 25 hello"
    print("\nActual message:", message2)
    print("Encrypted message:", encrypt_message(message2))

if __name__ == "__main__":
    main()
