def count_uppercase_characters():
    try:
        with open("ABC.txt", "r") as file:
            content = file.read()
            count = sum(1 for char in content if char.isupper())
            print("Total number of uppercase characters in 'ABC.txt':", count)
    except FileNotFoundError:
        print("The file 'ABC.txt' was not found.")
    except Exception as e:
        print("An error occurred:", e)
count_uppercase_characters()
