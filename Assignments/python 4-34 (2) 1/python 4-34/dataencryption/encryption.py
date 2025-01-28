def encrypt_message(message):
    # Function to shift a character to the next character
    def shift_char(char):
        if char.isalpha():  # Only shift alphabetic characters
            if char == 'z':
                return 'a'
            elif char == 'Z':
                return 'A'
            else:
                return chr(ord(char) + 1)
        elif char.isdigit():  # Increment digits and wrap-around at 9
            return str((int(char) + 1) % 10)
        return char  # Non-alphabetic and non-numeric characters remain the same

    # Process the string character by character
    encrypted_message = ''.join(shift_char(c) for c in message)

    return encrypted_message


def main():
    # Prompt user for input and display the result
    message = input("Actual message: ").strip()
    print(f"Encrypted message: {encrypt_message(message)}")

if __name__ == "__main__":
    main()