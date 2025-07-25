def login(username, password):
    if username == "admin" and password == "1234":
        return True
    else:
        return False
attempts = 0
try:
    while attempts < 3:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if login(user, pwd):
            print("Login successful!")
            break
        else:
            attempts += 1
            print(f"Invalid credentials. Attempts left: {3 - attempts}")
    if attempts == 3:
        raise PermissionError("Login failed 3 times. Access denied.")
except PermissionError as e:
    print("Error:", e)

