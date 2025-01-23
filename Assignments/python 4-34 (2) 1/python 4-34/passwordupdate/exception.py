class PasswordLengthException(Exception):
    """Raised when the password is shorter than 8 characters."""
    pass

class PasswordCaseException(Exception):
    """Raised when the password does not contain both uppercase and lowercase letters."""
    pass

class PasswordDigitException(Exception):
    """Raised when the password does not contain at least one digit."""
    pass

class PasswordSpecialCharException(Exception):
    """Raised when the password does not contain at least one special character."""
    pass
