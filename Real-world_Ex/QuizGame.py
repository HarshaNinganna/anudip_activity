questions = {
    "What is the capital of France?": {
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Rome"],
        "answer": "B"
    },
    "Which language is used for web apps?": {
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. All of the above"],
        "answer": "D"
    },
    "What is 5 + 7?": {
        "options": ["A. 10", "B. 12", "C. 14", "D. 15"],
        "answer": "B"
    }
}

score = 0

print(" Welcome to the Quiz Game!")
print("-" * 40)

for question, data in questions.items():
    print(f"\n{question}")
    for option in data["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    if answer == data["answer"]:
        print(" Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer is {data['answer']}.")

print("\n Quiz Completed!")
print(f"Your score: {score}/{len(questions)}")
