def count_words_in_file():
    try:
        with open("ABC.txt", "r") as file:
            content = file.read()
            words = content.split()
            print("Total number of words in 'ABC.txt':", len(words))
    except FileNotFoundError:
        print("The file 'ABC.txt' was not found.")
    except Exception as e:
        print("An error occurred:", e)
count_words_in_file()
