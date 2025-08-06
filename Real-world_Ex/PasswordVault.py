import json
import os

VAULT_FILE = "vault.json"

if not os.path.exists(VAULT_FILE):
    with open(VAULT_FILE, "w") as f:
        json.dump({}, f)

def load_vault():
    with open(VAULT_FILE, "r") as f:
        return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_password(website, username, password):
    vault = load_vault()
    vault[website] = {
        "username": username,
        "password": password
    }
    save_vault(vault)
    print(f" Saved credentials for {website}.")

def view_passwords():
    vault = load_vault()
    if not vault:
        print(" No passwords saved yet.")
    else:
        print("\n Stored Credentials:")
        for site, creds in vault.items():
            print(f"\n {site}")
            print(f"    Username: {creds['username']}")
            print(f"    Password: {creds['password']}")

def search_website(site):
    vault = load_vault()
    if site in vault:
        creds = vault[site]
        print(f"\n Found entry for {site}")
        print(f"    Username: {creds['username']}")
        print(f"    Password: {creds['password']}")
    else:
        print(" No credentials found for that website.")

def delete_website(site):
    vault = load_vault()
    if site in vault:
        del vault[site]
        save_vault(vault)
        print(f" Deleted credentials for {site}.")
    else:
        print(" Website not found in vault.")

def main():
    while True:
        print("\n--- Password Vault Menu ---")
        print("1. Add New Password")
        print("2. View All Passwords")
        print("3. Search Password by Website")
        print("4. Delete Password by Website")
        print("5. Exit")

        choice = input("Enter choice (1–5): ")

        if choice == "1":
            site = input("Enter website: ").lower()
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(site, username, password)

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            site = input("Enter website to search: ").lower()
            search_website(site)

        elif choice == "4":
            site = input("Enter website to delete: ").lower()
            delete_website(site)

        elif choice == "5":
            print(" Exiting Password Vault. Stay secure!")
            break

        else:
            print(" Invalid option. Please select 1–5.")

if __name__ == "__main__":
    main()
