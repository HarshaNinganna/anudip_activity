def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_digit
password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid")
else:
    print("Password is invalid")
