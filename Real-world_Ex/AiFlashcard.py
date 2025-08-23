import re

def generate_flashcards(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    flashcards = []

    for sentence in sentences:
            words = [w for w in re.findall(r'\b\w+\b', sentence)]
            if words:
                answer = words[0]
                question = f"What is this sentence talking about?\n\"{sentence}\""
                flashcards.append((question, answer))
    return flashcards


if __name__ == "__main__":
    print(" AI Flashcard Generator")
    print("Paste any paragraph to generate flashcards. Type 'exit' to quit.\n")

    while True:
        text = input("Enter text/paragraph: ")
        if text.lower() == "exit":
            print("Goodbye!  Keep learning with flashcards.")
            break

        flashcards = generate_flashcards(text)
        if not flashcards:
            print(" Not enough content to generate flashcards.\n")
        else:
            print("\n Generated Flashcards:\n")
            for i, (q, a) in enumerate(flashcards, 1):
                print(f"{i}. Q: {q}")
                print(f"   A: {a}\n")
