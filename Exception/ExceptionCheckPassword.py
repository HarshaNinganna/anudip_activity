def check_password(password):
    if len(password) < 8:
        raise ValueError("Weak password")
    else:
        print("Password accepted.")
try:
    user_password = input("Enter your password: ")
    check_password(user_password)
except ValueError as e:
    print("Error:", e)

