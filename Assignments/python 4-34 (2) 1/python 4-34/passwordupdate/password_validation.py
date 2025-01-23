import re
from exception import PasswordLengthException, PasswordCaseException, PasswordDigitException, PasswordSpecialCharException

def validate_password(new_password):
    # Check password length
    if len(new_password) < 8:
        raise PasswordLengthException("Password must be at least 8 characters long")
    
    # Check if password contains both uppercase and lowercase letters
    if not re.search(r'[a-z]', new_password) or not re.search(r'[A-Z]', new_password):
        raise PasswordCaseException("Password must contain both uppercase and lowercase letters")
    
    # Check if password contains at least one digit
    if not re.search(r'[0-9]', new_password):
        raise PasswordDigitException("Password must contain at least one digit")
    
    # Check if password contains at least one special character
    special_characters = r"!@#$%^&*(),.?\":{}|<>"
    if not any(char in special_characters for char in new_password):
        raise PasswordSpecialCharException("Password must contain at least one special character")
    
    # If all conditions are met
    return "Password updated successfully"
