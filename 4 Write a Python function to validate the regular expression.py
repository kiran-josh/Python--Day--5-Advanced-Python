"""
Name: Kiran G
Program: Write a Python function to validate the regular expression for the foollowing 

a. email address.
b. mobile numbers of Bangladesh
c. Telephone numbers of USA
d. 16 character alpha-numeric password composed of alphabets of upper case, lower case, special characters, Numbers 

"""

# email address------------------
import re

def validate_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Using re.match to check if the email matches the regex
    if re.match(email_regex, email):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    test_emails = [
        "example@example.com",
        "user.name+tag+sorting@example.com",
        "user.name@example.co.uk",
        "user@subdomain.example.com",
        "invalid-email@.com",
        "invalid-email@com.",
        "invalid@domain@domain.com",
        "user@domain..com"
    ]

    for email in test_emails:
        print(f"{email}: {validate_email(email)}")


# Mobile numbers of Bangladesh------------------------------- 

import re

def validate_bangladesh_mobile(mobile):
    # Regular expression for validating Bangladeshi mobile numbers
    mobile_regex = r'^01[3-9]\d{8}$'
    
    # Using re.match to check if the mobile number matches the regex
    if re.match(mobile_regex, mobile):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    test_numbers = [
        "01712345678",  # Valid
        "01812345678",  # Valid
        "01912345678",  # Valid
        "01612345678",  # Valid
        "01512345678",  # Invalid
        "01412345678",  # Invalid
        "1234567890",   # Invalid
        "0171234567",   # Invalid (only 7 digits after 01)
        "017123456789", # Invalid (too many digits)
        "017abcdefg",   # Invalid (contains letters)
    ]

    for number in test_numbers:
        print(f"{number}: {validate_bangladesh_mobile(number)}")




#Telephone numbers of USA----------------------

import re

def validate_usa_phone_number(phone):
    # Regular expression for validating US phone numbers
    phone_regex = r'^\+?1?\s*[-.()]?(\d{3})[-.()]?\s*(\d{3})[-.()]?(\d{4})$'
    
    # Using re.match to check if the phone number matches the regex
    if re.match(phone_regex, phone):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    test_numbers = [
        "(123) 456-7890",  # Valid
        "123-456-7890",    # Valid
        "1234567890",      # Valid
        "123.456.7890",    # Valid
        "+1 (123) 456-7890",  # Valid
        "+1 123-456-7890",     # Valid
        "123 456 7890",      # Valid
        "123-45-6789",       # Invalid (short)
        "(123) 456-78901",   # Invalid (too long)
        "123-456-789",       # Invalid (short)
        "abcd-456-7890",     # Invalid (letters)
    ]

    for number in test_numbers:
        print(f"{number}: {validate_usa_phone_number(number)}")



#16 character alpha-numeric password composed of alphabets of upper case, lower case, special characters, Numbers--------------

import re

def validate_password(password):
    # Regular expression for validating a 16-character alpha-numeric password
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{16}$'
    
    # Using re.match to check if the password matches the regex
    if re.match(password_regex, password):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    test_passwords = [
        "A1b2C3d4!@#$%^&*(",  # Valid
        "password12345678",    # Invalid (no uppercase, no special character)
        "PASSWORD12345678",    # Invalid (no lowercase, no special character)
        "Passw0rd!@#45678",     # Valid
        "Short1!",              # Invalid (too short)
        "NoSpecialCharacters123", # Invalid (no special character)
        "ValidPass12345!@#",    # Invalid (only 15 characters)
        "UpperCase!Lower12",    # Valid
    ]

    for pwd in test_passwords:
        print(f"{pwd}: {validate_password(pwd)}")




