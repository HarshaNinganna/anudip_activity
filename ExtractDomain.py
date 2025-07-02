def extract_domain(email):
    if "@" in email:
        domain = email.split("@")[1]
        return domain
    else:
        return "Invalid email"
email = input("Enter your email: ")
print("Domain:", extract_domain(email))
