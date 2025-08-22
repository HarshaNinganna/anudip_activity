from textblob import TextBlob

def grammar_check(text):
    blob = TextBlob(text)
    corrected = str(blob.correct())
    return corrected

if __name__ == "__main__":
    print("AI Grammar & Spell Checker")
    print("Type 'exit' to stop.\n")

    with open("corrected_notes.txt", "a", encoding="utf-8") as file:
        while True:
            user_input = input("Enter a sentence: ")
            if user_input.lower() == "exit":
                print("Goodbye! Corrections saved in corrected_notes.txt ")
                break

            corrected_text = grammar_check(user_input)
            print(f" Corrected: {corrected_text}\n")
            file.write(f"Original: {user_input}\nCorrected: {corrected_text}\n{'-'*40}\n")
