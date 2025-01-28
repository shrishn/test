from password_validation import validate_password
from exception import PasswordLengthException, PasswordCaseException, PasswordDigitException, PasswordSpecialCharException

def main():
    # Get user input for the new password
    new_password = input("Enter the new password: ")
    
    try:
        # Call the validate_password function
        result = validate_password(new_password)
        print(result)  # Password updated successfully
    except PasswordLengthException as e:
        print(f"Invalid password: {e}")
    except PasswordCaseException as e:
        print(f"Invalid password: {e}")
    except PasswordDigitException as e:
        print(f"Invalid password: {e}")
    except PasswordSpecialCharException as e:
        print(f"Invalid password: {e}")

if __name__ == "__main__":
    main()
