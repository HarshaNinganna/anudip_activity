from transformers import pipeline

# Load grammar correction model
grammar_corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

# Example sentences
sentences = [
    "She go to market yesterday.",
    "I has a new phone and it work good.",
    "He don't like playing football."
]

for text in sentences:
    corrected = grammar_corrector(text, max_length=64, do_sample=False)[0]['generated_text']
    print(f" Original: {text}")
    print(f" Corrected: {corrected}\n")
