import re

def check_password_strength(password):
    strength_points = 0
    suggestions = []

    if len(password) >= 8:
        strength_points += 1
    else:
        suggestions.append("Increase length to at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        suggestions.append("Add special characters.")

    if strength_points <= 2:
        rating = "Weak"
    elif strength_points == 3 or strength_points == 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, suggestions

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    rating, tips = check_password_strength(pwd)
    print(f"\nPassword Strength: {rating}")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(f" - {tip}")
