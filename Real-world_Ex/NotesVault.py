import os

NOTES_DIR = "notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def save_note(filename, content):
    try:
        with open(os.path.join(NOTES_DIR, filename), 'w') as f:
            f.write(content)
        return f" Note '{filename}' saved successfully."
    except Exception as e:
        return f" Error saving note: {e}"

def read_note(filename):
    try:
        with open(os.path.join(NOTES_DIR, filename), 'r') as f:
            content = f.read()
        return f" Contents of '{filename}':\n{content}"
    except FileNotFoundError:
        return f" Note '{filename}' not found."
    except Exception as e:
        return f" Error reading note: {e}"

def delete_note(filename):
    try:
        os.remove(os.path.join(NOTES_DIR, filename))
        return f" Note '{filename}' deleted successfully."
    except FileNotFoundError:
        return f" Note '{filename}' not found."
    except Exception as e:
        return f" Error deleting note: {e}"

def list_notes():
    try:
        files = os.listdir(NOTES_DIR)
        return f" Saved Notes:\n" + "\n".join(files) if files else " No notes found."
    except Exception as e:
        return f" Error listing notes: {e}"

def main():
    while True:
        print("\n--- NoteVault Menu ---")
        print("1. Save Note\n2. Read Note\n3. Delete Note\n4. List Notes\n5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            filename = input("Enter filename (with .txt): ")
            content = input("Enter your note content:\n")
            print(save_note(filename, content))

        elif choice == "2":
            filename = input("Enter filename to read: ")
            print(read_note(filename))

        elif choice == "3":
            filename = input("Enter filename to delete: ")
            print(delete_note(filename))

        elif choice == "4":
            print(list_notes())

        elif choice == "5":
            print(" Exiting NoteVault. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    main()
