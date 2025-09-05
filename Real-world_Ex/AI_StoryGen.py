from transformers import pipeline

def generate_story(prompt, max_length=150):
    generator = pipeline("text-generation", model="gpt2")
    
    # Generate story
    story = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=1,
        truncation=True
    )
    
    return story[0]['generated_text']

if __name__ == "__main__":
    print("=== AI Story Generator ===")
    topic = input("Enter a topic or beginning line: ")
    story = generate_story(topic)
    
    print("\n Generated Story:\n")
    print(story)
