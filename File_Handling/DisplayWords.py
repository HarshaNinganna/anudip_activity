def display_words():
    try:
        with open("story.txt", "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print("The file 'story.txt' was not found.")
    except Exception as e:
        print("An error occurred:", e)
display_words()
