def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    return True
try:
    email_input = input("Enter your email: ")
    if validate_email(email_input):
        print("Email accepted:", email_input)
except ValueError as e:
    print("Error:", e)
