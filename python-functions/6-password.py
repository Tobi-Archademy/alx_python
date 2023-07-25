#!/usr/bin/python3
def validate_password(password):
    emp_space = " "
    if (len(password) < 8):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if any(char in emp_space for char in password):
        return False
    return True