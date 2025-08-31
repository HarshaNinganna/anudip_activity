from transformers import pipeline

def ai_chatbot():
    chatbot = pipeline(
        "text-generation",
        model="gpt2",
        pad_token_id=50256  
    )

    print("=== AI Chatbot ===")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print(" Goodbye!")
            break

        response = chatbot(
            user_input,
            max_new_tokens=100,    
            truncation=True,       
            num_return_sequences=1
        )

        ai_text = response[0]["generated_text"].replace(user_input, "").strip()
        print("AI:", ai_text)


if __name__ == "__main__":
    ai_chatbot()
