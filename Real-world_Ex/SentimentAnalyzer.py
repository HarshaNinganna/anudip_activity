from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    print("Day 22 of #75DaysOfCode — AI Sentiment Analyzer")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("Enter a sentence: ")
        if user_input.lower() == "exit":
            print("Exiting Sentiment Analyzer. Goodbye!")
            break

        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}\n")
