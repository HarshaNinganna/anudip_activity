import requests

def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        data = response.json()

        if isinstance(data, dict) and data.get("title") == "No Definitions Found":
            print(f" No definition found for '{word}'.")
            return

        print(f"\n Word: {data[0]['word']}")
        print(f" Phonetic: {data[0].get('phonetic', 'N/A')}")

        # Print first 2 meanings
        for meaning in data[0]["meanings"][:2]:
            part_of_speech = meaning["partOfSpeech"]
            definition = meaning["definitions"][0]["definition"]
            example = meaning["definitions"][0].get("example", "No example")
            print(f"\n {part_of_speech.capitalize()}")
            print(f"   • Meaning: {definition}")
            print(f"   • Example: {example}")

    except Exception as e:
        print(" Error fetching data:", e)


if __name__ == "__main__":
    print("=== Dictionary App ===")
    word = input("Enter a word: ").strip()
    get_word_meaning(word)
    
