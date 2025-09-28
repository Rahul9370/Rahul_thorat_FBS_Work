"""5. Write a Python function that takes an email address as input and uses a regular
expression to validate if it is a valid email address. The function should return True for
valid emails and False for invalid ones."""
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$'
    if re.match(pattern, email):
        return True
    else:
        return False

print(validate_email("test@example.com"))    # True
print(validate_email("hello.world@domain.in"))  # True
print(validate_email("invalid-email@.com"))     # False
print(validate_email("abc@domain"))             # False
