import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_texts = [
    "Python is a programming language",
    "The Earth revolves around the Sun",
    "Water boils at 100 degrees Celsius",
    "Let's hang out this weekend",
    "Are you coming to the party?",
    "Hey, what's up?",
]
training_labels = [
    "educational", "educational", "educational",
    "casual", "casual", "casual"
]

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_texts)

model = MultinomialNB()
model.fit(X_train, training_labels)

def generate_flashcards(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    flashcards = []

    for sentence in sentences:
        words = [w for w in re.findall(r'\b\w+\b', sentence)]
        if words:
            answer = words[0]
            question = f"What is this sentence talking about?\n\"{sentence}\""

            X_test = vectorizer.transform([sentence])
            category = model.predict(X_test)[0]

            flashcards.append((question, answer, category))
    return flashcards


if __name__ == "__main__":
    print(" AI Flashcard Generator + Classifier")
    print("Paste any paragraph to generate categorized flashcards. Type 'exit' to quit.\n")

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
            for i, (q, a, c) in enumerate(flashcards, 1):
                print(f"{i}. Q: {q}")
                print(f"   A: {a}")
                print(f"   Category: {c}\n")
